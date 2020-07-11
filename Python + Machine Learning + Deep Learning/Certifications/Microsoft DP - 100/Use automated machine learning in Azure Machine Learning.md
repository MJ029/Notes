### What is Machine Learning:
- Machine learning is a technique that uses mathematics and statistics to create a model that can predict unknown values.
- It is data driven approach.
- Ex:
	- A Cycle company that rents cycles in a city wants to predict daily rental demand. In-order to perform that you need below factors
		- one or more number of features(X)
		- predicted label (y)
		- Mathematical function f(x)
	- f(X) = y
	- In the above example the details about a given day (day of the week, weather, and so on) are the features (x).
	- The number of rentals for that day is the label (y)
	- Function f(X), predicts the number of rentals based on the information is encapsulated in a machine learning model.

Note:
- Training and deploying an effective machine learning model involves a lot of work, much of it time-consuming and resource-intensive. 
- But there are some readymade services available[such as AzureML-Service, Amazon Seagemager and etc...] in-ourder ro reduce the work load

### Create an Azure Machine Learning workspace:
- Go to [azure portal](https://portal.azure.com/#home) and click create resource then search and select **new Machine Learning** resource.
- The below listed properties are important when creating Azure ML resource.
	- Workspace Name
	- Subscription
	- Resource group
	- Location
	- Workspace edition
- Fill the above fields and click create button, It will create new Azure ML workspace wait for some time and navigate to **Home** tab you can see your resources created.
- On the Overview page for your workspace, launch Azure Machine Learning studio (or open a new browser tab and navigate to https://ml.azure.com ), and sign into Azure Machine Learning studio using your Microsoft account.
- Choose Subscription and resourcegorup and ML flow in next window and click launch.

Note:
- Make sure that your subscription and resource group were created already and valid.

### Create compute resources:
- Compute resources are cloud-based resources on which you can run model training and data exploration processes.
- It is also known as compute targets.
- Types of compute resources:
	- **Compute Instances (***dev-instance***):** Development workstations that data scientists can use to work with data and models.
	- **Compute Clusters (***train-instance***) :** Scalable clusters of virtual machines for on-demand processing of experiment code.
	- **Inference Clusters (***test/prod-instance***):** Deployment targets for predictive services that use your trained models.
	- **Attached Compute (***external services***):** Links to existing Azure compute resources, such as Virtual Machines or Azure Databricks clusters.

- To add new compute instance click **create** in **compute instance** tab and enter below fields, In background it will create Databricks cluster
	- **Compute name:** Unique name
	- **Virtual Machine type:** CPU/GPU 
	- **Virtual Machine size:** Standard Databricks Cluster VM config name
- While the compute instance is being created, switch to the Compute Clusters tab, and add a new compute cluster with the following settings. You'll use this to train a machine learning model:
- To add a new Compute cluster click **creat** in **compute clusters** tab and enter the below fields. In background it will create Databricks cluster
	- **Compute name:** enter a unique name
	- **Virtual Machine size:** Standard Databricks Cluster VM config name
	- **Virtual Machine priority:** Dedicated
	- **Maximum number of nodes:** MAximum required nodes to tain your model.
	- **Minimum number of nodes:** Minimum required nodes to tain your model. This will always keep 2 clusters up and running so it is recommended to set 0, then cluster will be spin up during only training execution.
	- **Idle seconds before scale down:** Keep alive time used to keep the cluster up and running idle for specified duration.

### Explore data:
- Machine learning models must be trained with existing data. 
- DataSet:
	- In Azure Machine Learning, **data** for model training and other operations is usually encapsulated in an object called a **dataset**.
	- In [Azure Machine Learning studio](https://ml.azure.com/) , view the Datasets page (under Assets), and create a new dataset.
	- We can create dataset from below listed sources.
		- **From Local File system:** Allows user to load data from local storage.
		- **From datastore:** Allows user to load data from datastore.
		- **From web files:** Allows user to load data from web scraps and web API's.
		- **From Open Dataset:** Allows user to load data from Open Dataset.
	- Each type takes its own set of input parameters
	
	- Ex (WEB-API):
		- To simulate the above usecase we leared in [What is Machine Leraning page](#what-is-machine-learning) we need to load data from below web API [https://aka.ms/bike-rentals](https://aka.ms/bike-rentals).
		- In-order to load data from web-api we need below list of parameters.
			- **Basic Info:**
				- **URL:** source API url to be scrapped.
				- **Name:** Unique dataset name.
				- **Dataset Type:** Tabular/File.
				- **Description:** More detail about the data.
				- **Skip data validation (checkbox):** Optional if enabled it will perform data validation while loading.
			- **Settings and preview:**
				- **File format:** Used to specify the file format.
				- **Delimiter: ** used to specify the delimiter.
				- **Encoding:** Used to specify the encoding standard.
				- **Column headers:** Used to specify the column header info.
				- **Skip Rows:** Used to specify the skip rows when reading file.
			- **Schema:**
				- Automatically detect schema and load its type.
				- Used to alred autodetected schema definition.
		- After the dataset has been created, open it and view the Explore page to see a sample of the data. This data contains historical features and labels for bike rentals.

### Train a machine learning model:
- 
- 