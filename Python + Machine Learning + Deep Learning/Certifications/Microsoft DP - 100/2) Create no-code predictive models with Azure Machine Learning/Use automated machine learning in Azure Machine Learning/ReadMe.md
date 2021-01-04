## Table of Content
[What is machine Learning](#what-is-machine-learning)  
[Create Azure Maxhine Learning Workspace](#create-an-azure-machine-learning-workspace)  
[Create Compute Resources](#create-compute-resources)  
[Explore Data](#explore-data)  
[Train Machine Learening Model](#train-a-machine-learning-model)  
[Deploy Model as a Serivice](#deploy-a-model-as-a-service)  

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
- Azure Machine Learning is a cloud-based platform for building and operating machine learning solutions in Azure. 
- It includes a wide range of features and capabilities that help data scientists prepare data, train models, publish predictive services, and monitor their usage.
- Most importantly, it helps data scientists increase their efficiency by automating many of the time-consuming tasks associated with training models; and it enables them to use cloud-based compute resources that scale effectively to handle large volumes of data while incurring costs only when actually used.
- Go to [azure portal](https://portal.azure.com/#home) and click create resource then search and select **new Machine Learning** resource.
- The below listed properties are important when creating Azure ML resource.
	- Workspace Name
	- Subscription
	- Resource group
	- Region
	- Storage account
	- Key Vault
	- Application insights
	- Container registry
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
	- **Enable SSH access:** Unselected
- While the compute instance is being created, switch to the Compute Clusters tab, and add a new compute cluster with the following settings. You'll use this to train a machine learning model:
- To add a new Compute cluster click **creat** in **compute clusters** tab and enter the below fields. In background it will create Databricks cluster
	- **Compute name:** enter a unique name
	- **Virtual Machine size:** Standard Databricks Cluster VM config name [***ex:*** Standard_DS11_v2]
	- **Virtual Machine type:** CPU
	- **Virtual Machine priority:** Dedicated
	- **Maximum number of nodes:** Maximum required nodes to tain your model.
	- **Minimum number of nodes:** Minimum required nodes to tain your model. This will always keep 2 clusters up and running so it is recommended to set 0, then cluster will be spin up during only training execution.
	- **Idle seconds before scale down:** Keep alive time used to keep the cluster up and running idle for specified duration.
	- **Enable SSH access:** Unselected

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
				- **Delimiter:** used to specify the delimiter.
				- **Encoding:** Used to specify the encoding standard.
				- **Column headers:** Used to specify the column header info.
				- **Skip Rows:** Used to specify the skip rows when reading file.
			- **Schema:**
				- Automatically detect schema and load its type.
				- Used to alter autodetected schema definition.
		- After the dataset has been created, open it and view the Explore page to see a sample of the data. This data contains historical features and labels for bike rentals.

### Train a machine learning model:
- Azure Machine Learning includes an automated machine learning capability that leverages the scalability of cloud compute to automatically try multiple pre-processing techniques and model-training algorithms in parallel to find the best performing model for your data.
- In Azure Machine Learning, ***operations*** that you run are called **experiments**.
- Currently we cannot delete exprements from UI we have only powershell commands to delete exprements.

- In [Azure Machine Learning studio](https://ml.azure.com/), view the **Automated ML** page (under **Author** section).
- Follow below steps to create a new Automated ML and run it.
	- **Select dataset:**
		- Choose the dataset that has been created earlier, if not you will be having an option to create a new dataset in teh same page.
	- **Configure run:**
		- **New experiment name:** Unique expriment Name.
		- **Target column:** Specifies target column in dataset to be used as predictor(Y)
		- **Training compute target:** Choose the **Compute Clusters** that created previously
	- **Task type and settings:**
		- **Task type:** Specifies type of task (**Regression**, **Classification**, **Time Series**)
		- **Additional configuration settings:**
			- **Primary metric:** Specifies metrics availabel for regression and classification models like MSE, MAE and etc...
      			- Classification:
    				- Accuracy
    				- AUC Weight
    				- Norm Macro recall
    				- Average precision score weighted
    				- Precision score weighted
    			- Regression:
    				- Spearman Correlation
    				- Normelized root mean squared error
    				- R2 Score
    				- Normalized mean squared error
    			
    			- Time Series:
    				- Normelized root mean squared error
    				- R2 Score
    				- Normalized mean squared error
    				
    			- Validations:
    				- k-fold cross validation
    				- Monte carlo cross validation
    				- Train-validation split
    				- Auto			
			- **Explain best model:** Checkbox, this option causes automated machine learning to calculate feature importance for the best model; making it possible to determine the influence of each feature on the predicted label.
			- **Blocked algorithms:** Specifies that algorithms not the be performed.
    			- **Regression:**
    				- ElasticNet
    				- GradientBoosting
    				- Decision Tree
    				- KNN
    				- LassoLars
    				- SGD
    				- RandomForest
    				- ExtreemRandomTrees
    				- LightGBM
    				- XGBoostRegressor
    				- FastLinearRegression
    				- OnlineGradientRegressor
    			- **Classification:**
    				- LogisticRegression
    				- SGD
    				- MultinomialNaiveBayes
    				- BernouliNaiveBayes
    				- SVM
    				- LinearSVM
    				- KNN
    				- DecisionTree
    				- RandomForest
    				- ExtremeRandomTrees
    				- LightGBM
    				- GradientBoosting
    				- XGBoostClassifier
    				- AveragedPerceptronClassifier
    			- **TimeSeries Forecasting:**
    				- AutoArima
    				- Prophet
    				- TCNForecaster
    				- ElasticNet
    				- GradientBoosting
    				- DecisionTree
    				- KNN
    				- LassoLars
    				- SGD
    				- RandomForest
    				- ExtreemRandomTrees
    				- LightGBM
    				- XGBoostRegressor
    		- **Exit Criterian:** Specifies the threshold to exit from job training. usually it will be Time bound or Metric bound.
        		- **Training job time (hours):** The maximum amount of time, in hours, for an experiment to train the models.
        		- **Metric score threshold:** When this threshold value will be reached for an iteration metric the training job will terminated.
            		- ***Note:*** Keep in mind that meaningful models have correlation > 0, otherwise they are as good as guessing the average Metric threshold should be between bounds -1 - 1
      		- **Validation:** Specifies type of validation we are going to use in our expriment.
        		- **Validation type:** 
            		- Auto
            		- K-Fold Cross Validation
            		- Monte Carlo Cross Validation
            		- Train-Validation Split
      		- **Concurrency:** Specifies maximum parallel Iterations to run.
        		- **Max concurrent iterations:** Integer Value >= 1
  		- **Featurization settings:**
    		- **Enable featurization:** Selected - this causes Azure Machine Learning to automatically preprocess the features before training.

### Deploy a model as a service:
- After you've used automated machine learning to train some models, you can deploy the best performing model as a service for client applications to use.
- In Azure Machine Learning, you can deploy a service as an **Azure Container Instances (ACI)** or to an **Azure Kubernetes Service (AKS)** cluster.
- For production scenarios, an AKS deployment is recommended. [for which you must create an inference cluster compute target.]
- In [Azure Machine Learning studio](https://ml.azure.com/)), on the Automated ML page, select the run for your automated machine learning experiment and view the Details tab.
- Select the algorithm name for the best model.
- Goto Model tab, use the Deploy button to deploy the model
- Use the following setting to deploy the model.
	- **Name:** Unique Name
	- **Description:** More detail about the deployment.
	- **Compute type:** ACI/AKS
	- **Enable authentication:** checkbox to used to enable authentication
- Once after filling above information click deploy and wait for sometime till the deployment to finish.
- To check model deployment status use **Model summary** section in same model page. The status will be running wait for it to show as Successfull.
- Once after successfull click deployment name will take you to deployment page, Click **endpoint tab --> consume** page and notedown below information.
	- **URL:** The REST endpoint for your service
	- **key:** he Primary Key for your service
	
Note:  
	- To delete a model you need to delete the endpoint first.  
	- To delete the endpoint go to **EndPoints** in ***Assets*** the select the end point and click delete.  
	- Then click **Models** in ***Assets*** Select the model and click delete.

### Test the deployed service:
