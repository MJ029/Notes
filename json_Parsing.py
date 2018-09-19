import requests
import sys
import json
import math
import xml.etree.ElementTree

# Defining Needed Dictionaries
metricsDictionary = {}
queueDictionary = {}
sparkConf = {}
executorConf = {}

# To get Namenode information from hdfs-site.xml
def getNameNodeInfo(siteXml):
        nodeName = []
        hdfsSiteXml = xml.etree.ElementTree.parse(siteXml).getroot()
        for elem in hdfsSiteXml.findall('property'):
                hname = elem.find('./name').text
                if (hname.startswith("dfs.namenode.http-address.")):
                        hval = elem.find("./value").text
                        nodeName.append(hval.split(':')[0])
        return nodeName

# To get Active and Standby NameNode from the available node information
def getActiveNameNode(siteXml):
        rpcNameList = getNameNodeInfo(siteXml)
        url = "http://"+rpcNameList[0]+":8088/ws/v1/cluster/"
        resp = requests.get(url + "info")
        obj = json.loads(resp.content)
        #print(json.dumps(obj, indent=2, sort_keys=True))
        if obj["clusterInfo"]["haState"] == "ACTIVE":
                return url
        else:
                url = "http://"+rpcNameList[1]+":8088/ws/v1/cluster/"
                return url
serverName = getActiveNameNode(sys.argv[1])

# To get Cluster Metrics for active cluster
def getclusterMetrics(serverName):
        url = serverName + "metrics"
        resp = requests.get(url)
        obj = json.loads(resp.content)
        metricsDictionary["activeNodes"] = obj["clusterMetrics"]["activeNodes"]
        metricsDictionary["availableMB"] = obj["clusterMetrics"]["availableMB"]
        metricsDictionary["availableVirtualCores"] = obj["clusterMetrics"]["availableVirtualCores"]
        metricsDictionary["totalMB"] = obj["clusterMetrics"]["totalMB"]
getclusterMetrics(serverName)

# To get Queue Metrics for the given queue
def getQueueMetrics(serverName, activeQueue):
        url = serverName + "scheduler"
        resp = requests.get(url)
        obj = json.loads(resp.content)
        availableQueus = len(obj[u"scheduler"][u"schedulerInfo"][u"queues"][u"queue"])
        for i in range(availableQueus):
                if obj[u"scheduler"][u"schedulerInfo"][u"queues"][u"queue"][i]["queueName"] == activeQueue:
                        # To Derive absolute capacity from the queue metrics:
                        abCap = obj[u"scheduler"][u"schedulerInfo"][u"queues"][u"queue"][i]["absoluteCapacity"]
                        abCap = int((metricsDictionary["totalMB"] / 100) * abCap)
                        queueDictionary["absoluteCapacity"] = abCap

                        # To derive absolute Max capacity of the queue
                        abMaxCap = obj[u"scheduler"][u"schedulerInfo"][u"queues"][u"queue"][i]["absoluteMaxCapacity"]
                        abMaxCap = int((metricsDictionary["totalMB"] / 100) * abMaxCap)
                        queueDictionary["absoluteMaxCapacity"] = abMaxCap

                        # To derive absolute used capacity of the queue
                        abUsedCap = obj[u"scheduler"][u"schedulerInfo"][u"queues"][u"queue"][i]["absoluteUsedCapacity"]
                        abUsedCap = int((metricsDictionary["totalMB"] / 100) * abUsedCap)
                        queueDictionary["absoluteUsedCapacity"] = abUsedCap

                        # Running Application in Queue
                        queueDictionary["numActiveApplications"] = obj[u"scheduler"][u"schedulerInfo"][u"queues"][u"queue"][i]["numActiveApplications"]

                        # To Determine Queue Utilization
                        queueUtilization = (float(abUsedCap)/float(abMaxCap)) * 100
                        queueDictionary["queueUtilization"] = int(math.floor(queueUtilization))
getQueueMetrics(serverName, sys.argv[2])

# To get the Spark Job Configuration
def getSparkConf():
        totalCores = metricsDictionary["availableVirtualCores"]
        sparkConf["totalCores"]= totalCores

        totalExecutors = int(totalCores/5)
        sparkConf["totalExecutors"] = totalExecutors

        executorMemory = int(metricsDictionary["availableMB"] / totalExecutors / 1024)
        #executorMemory = int(metricsDictionary["totalMB"] / totalExecutors / 1024)
        sparkConf["executorMemory"] = executorMemory
getSparkConf()

# To get the Spark Job Final Configuration
def getFinalconf(dataSize):
        defaultReservedMemory = sparkConf["executorMemory"] * 90/100
        defaultCacheMemory = defaultReservedMemory * 60/100
        executorMemory = math.floor(defaultCacheMemory)
        executorCores = 0
        for i in range(1,sparkConf["totalExecutors"]):
                if (i * executorMemory <= int(dataSize)):
                        executorCores = i + 1
        executorConf["numExecutors"]= executorCores
        executorConf["executorCores"] = 4
getFinalconf(sys.argv[3])


# Outputs the numExecutors, executorCores, executorMemory, queueUtilization, numActiveApplications to Shell Variable
if executorConf["numExecutors"] != 0 and sparkConf["executorMemory"] != 0:
        print(str(executorConf["numExecutors"]) +":" +str(executorConf["executorCores"]) +":"+ str(sparkConf["executorMemory"])
              + ":" + str(queueDictionary["queueUtilization"])+ ":" + str(queueDictionary["numActiveApplications"]))
else:
        print("No Executors available on the Queue, wait for sometime...!")
