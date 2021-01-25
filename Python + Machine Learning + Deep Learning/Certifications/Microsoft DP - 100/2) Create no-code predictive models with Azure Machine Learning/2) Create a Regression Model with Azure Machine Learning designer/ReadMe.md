### Introduction:
- In nutshell, Regression is a form of machine learning that is used to predict a numeric label based on an item's features.
- For example, an automobile sales company might use the characteristics of car (such as engine size, number of seats, mileage, and so on) to predict its likely selling price.
- In this case, the characteristics of the car are the features, and the selling price is the label.
- Regression is an example of a supervised machine learning technique.
- In nutshell, supervised learning is a technique where you train a model using data that includes both the features and known values for the label, so that the model learns to fit the feature combinations to the label.
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

### Explore Data:
- To train a regression model, you need a dataset that includes historical features (characteristics of the entity for which you want to make a prediction) and known label values (the numeric value that you want to train a model to predict).

#### Create a Pipeline:
- To use the Azure Machine Learning designer, you create a pipeline that you will use to train a machine learning model.
- in [Azure Machine Learning studio](https://ml.azure.com/), view the **Designer page** (under ***Author***), and select **+** to create a new pipeline.
- In the Settings pane, change the default pipeline name (Pipeline-Created-on-date) to your suitable name.
- use the setting icon in the screen to enable/diable setting page in screen.
- Selct dataset tab and dragdown the input dataset required for the model.
- Select modules table and dragdown the required transofrmation moduels form available categories and build your transformation pipeline.
- 