# Train and evaluate regression models

### Objective:
- When to use regression models.
- How to train and evaluate regression models using the Scikit-Learn framework.

### Pre-Requisites:
- Basic Knowledge on Mathematics.
- Basic Knowledge on Python.
- Microsoft Azure Subscription
- [Azure Machine Learning workspace](https://ml.azure.com/)
- Azure Machine Learning compute instance
- [Azure ml-basics repository](https://github.com/microsoftdocs/ml-basics)

## Table Of Content
[1. Introduction](#1-introduction)  
[2. Explore Data](#2-explore-data)  
[3. Jupyter Notebook](#3-jupyter-notebook)  

### 1. Introduction
- Regression is a form of machine learning in which the goal is to create a model that can predict a numeric, quantifiable value; such as a price, amount, size, or other scalar number.
- Regression works by establishing a relationship between variables in the data that represent characteristics (known as the features) of the thing being observed, and the variable we're trying to predict (known as the label).
- A training dataset to which we'll apply an algorithm that determines a function encapsulating the relationship between the feature values and the known label values.
- A validation or test dataset that we can use to evaluate the model by using it to generate predictions for the label and comparing them to the actual known label values.

### 2. Explore data
- Data exploration and analysis is typically an iterative process, in which the data scientist takes a sample of data, and performs the following kinds of task to analyze it and test hypotheses
	- Clean data to handle errors, missing values, and other issues.
	- Apply statistical techniques to better understand the data, and how the sample might be expected to represent the real-world population of data, allowing for random variation.
	- Visualize data to determine relationships between variables, and in the case of a machine learning project, identify features that are potentially predictive of the label.
	- Derive new features from existing ones that might better encapsulate relationships within the data.
	- Revise the hypothesis and repeat the process.
- Data scientists can use a variety of tools and techniques to explore, visualize, and manipulate data. 

#### Note:
- The below listed items Tutorial can be found [here](https://github.com/MicrosoftDocs/ml-basics/blob/master/01%20-%20Data%20Exploration.ipynb)

### 3. Jupyter Notebook
- Exploring data arrays with NumPy:
  - List/Numpy Array Creation & Differrence
-  Exploring tabular data with Pandas:
   -  Pandas Dataframe Introduction
   -  Pandas Dataframe Creation
   -  Filtering Pandas Dataframe **[loc, iloc, filter expression, query]**
   -  Creating Dataframe from a file
   -  Handling Missing Values **[fill, drop]**
   -  Descriptive Statistics **[mean, median, mode, groupby & sortvalues]**
-  Visualizing data with Matplotlib:
   -  Visualizing bar plot
   -  Create plot with figsize
   -  Creating subplots
   -  Utilizing pandas.dataframe.plot Extension
-  Getting started with statistical analysis:
   -  Descriptive statistics and data distribution
      -  Data Distribution (Histogram)
      -  Measures of central tendency **[mean, median, mode, min, max]**
      -  Data Distribution (BoxPlot)
      -  Data Density (Density Plot) **Skewness**
      -  Measures of variance
         -  Range
         -  Variance
         -  Standard Deviation
      -  Value Comparision