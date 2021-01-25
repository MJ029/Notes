# Introduction to the Azure Machine Learning SDK
- Azure Machine Learning provides a cloud-based platform for training, deploying, and managing machine learning models

#### Objectives:
- Provision an Azure Machine Learning workspace.
- Use tools and interfaces to work with Azure Machine Learning.
- Run code-based experiments in an Azure Machine Learning workspace.

#### Prerequisites:
- Basic Knowledge on Python.
- Experience of training machine learning models using frameworks such as scikit-learn.

### Introduction:
- Azure Machine Learning is a platform for operating machine learning workloads in the cloud.
- Advantages:
  - Scalable on-demand compute for machine learning workloads.
  - Data storage and connectivity to ingest data from a wide range sources.
  - Machine learning workflow orchestration to automate model training, deployment, and management processes.
  - Model registration and management, so you can track multiple versions of models and the data on which they were trained.
  - Metrics and monitoring for training experiments, datasets, and published services.
  - Model deployment for real-time and batch inferencing.
![Alt text](Azure-Machine-Learning-Features.jpg?raw=true "Azure Machine Learning Tech-Stack")
<p style="text-align: center;"><b>Source:</b> https://docs.microsoft.com/</p>

### Azure Machine Learning workspaces:
- A workspace defines the boundary for a set of related machine learning assets. 
- It is a context for the experiments, data, compute targets, and other assets associated with a machine learning workload.
- It will help us to group machine learning assets based on projects, environments (ex:dev, test & prod), teams, or some other organizing principle.
- The asset includes the folowing:
  - Compute targets for development, training, and deployment.
  - Data for experimentation and model training.
  - Notebooks containing shared code and documentation.
  - Experiments, including run history with logged metrics and outputs.
  - Pipelines that define orchestrated multi-step processes.
  - Models that you have trained.

![Alt text](Azure-workspace.png?raw=true "Azure Machine Learning Tech-Stack")
<p style="text-align: center;"><b>Source:</b> https://docs.microsoft.com/</p>

- There are several other Azure resources that created alongside Azure Workspace creation as listed below.
  - **Storage Account:** store files used by the workspace as well as data for experiments & model training.
  - **Application Insights:** used to monitor predictive services in the workspace.
  - **Azure Key Vault:** used to manage secrets such as authentication keys and credentials used by the workspace.
  - **Container registry:** Created as-needed to manage containers for deployed models.

#### Note:
- You can assign role-based authorization policies to a workspace, enabling you to manage permissions that restrict what actions specific Azure Active Directory (AAD) principals can perform. 

### Creating a Workspace:
- ***Azure Portal:***
  - In the Microsoft Azure portal, create a new Machine Learning resource, specifying the subscription, resource group and workspace name. For more details [click here](https://microsoftlearning.github.io/mslearn-dp100/instructions/01-create-a-workspace.html)
- ***Python:***
  - Use the Azure Machine Learning Python SDK to run code that creates a workspace. 
	```
	from azureml.core import Workspace
	ws = Workspace.create(name='aml-workspace', 
						subscription_id='123456-abc-123...',
						resource_group='aml-resources',
						create_resource_group=True,
						location='eastus'
						)
	```
- ***CLI:***
  - Use the Azure Command Line Interface (CLI) with the Azure Machine Learning CLI extension.
	```
	az ml workspace create -w 'aml-workspace' -g 'aml-resources'
	```

