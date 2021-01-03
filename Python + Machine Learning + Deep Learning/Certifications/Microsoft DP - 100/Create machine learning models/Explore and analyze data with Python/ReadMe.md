# Explore and analyze data with Python

### Objective:
- Common Data Exploration and Analysis tasks.
- Python packages[Numpy, Pandas, Matplotlib] usage.

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
- Machine learning is a subset of data science that deals with predictive modeling. In other words, using data to create models that can predict unknown values.
- It works by identifying relationships between data values that describe characteristics of something (its features) and the value we want to predict (the label), and encapsulating these relationships in a model through a training process.

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