### Introduction:
- In nutshell, Regression is a form of machine learning that is used to predict a numeric label based on an item's features.
- For example, an automobile sales company might use the characteristics of car (such as engine size, number of seats, mileage, and so on) to predict its likely selling price.
- In this case, the characteristics of the car are the features, and the selling price is the label.
- Regression is an example of a supervised machine learning technique.
- In suthsell, supervised learning is a technique where you train a model using data that includes both the features and known values for the label, so that the model learns to fit the feature combinations to the label.

# Create compute resources:
- Most of the points covered in Module-1 already except below snippets.
- The **Compute Instances** and **Compute Clusters** were used in AutoML model, where we need to create one more instance called **Inference Clusters** in-order to deploy your model as a service.
- This step is automated in AutoML task [Module-1]
- To create a new **Inference Clusters** follow the below steps:
	- Login to ML workspace using [Azure Machine Learning studio](https://ml.azure.com/), then click **Compute** in ***Manage*** section in left side menu.
	- Navigate to **Inference Clusters** tab and click create button and enter the below fields to create new cluster.
	- **Compute name:** Unique Name for the cluster.
	- **Kubernetes Service:** Create New button.
	- **Region: ** use your region.
	- **Virtual Machine size:** Standard_DS2_v2
	- **Cluster purpose:** select dev-test radio button.
	- **Number of nodes:** 2
	- **Network configuration:** Basic
	- **Enable SSL configuration:** Unselected

# Explore Data:
- To train a regression model, you need a dataset that includes historical features (characteristics of the entity for which you want to make a prediction) and known label values (the numeric value that you want to train a model to predict).
- To use the Azure Machine Learning designer, you create a pipeline that you will use to train a machine learning model.
- in [Azure Machine Learning studio](https://ml.azure.com/), view the **Designer page** (under ***Author***), and select **+** to create a new pipeline.
- In the Settings pane, change the default pipeline name (Pipeline-Created-on-date) to your suitable name.
- use the setting icon in the screen to enable/diable setting page in screen.
- Selct dataset tab and dragdown the input dataset required for the model.
- Select modules table and dragdown the required transofrmation moduels form available categories and build your transformation pipeline.
- 