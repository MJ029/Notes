# Classification - Important Points
- In statistics, ***Classification*** is the problem of identifying to which of a set of **categories** (sub-populations) a **new observation** belongs, on the basis of a training set of data containing **observations** (or instances) whose category membership is known.
- In Simple,  ***Classification*** refers to a **predictive** modeling problem where a **class label** is predicted for a given example of input data.
- In the terminology of machine learning, **classification** is considered an instance of ***supervised learning***, i.e., learning where a training set of correctly identified observations is available. 
- The corresponding ***unsupervised*** procedure is known as **clustering**, and involves grouping data into categories based on some measure of **inherent** similarity or **distance**.
- We can use Classification algorithms in 4 ways.
  - Binary Classification
  - Multi-Class Classification
  - Multi-Label Classification
  - Imbalanced Classification

### Assumptions:
- **TODO**: Need to check for Assumptions on Classification problem.


## Linear Classifiers:

### 1. Binary Classification:
- ***Binary classification*** refers to those classification tasks that have two class labels.
- In Simple, Classification is a process of categorizing a given set of data into classes, It can be performed on both structured or unstructured data.
- Typically, binary classification tasks involve one class that is the normal state and another class that is the abnormal state.
- It is common to model a **binary** classification task with a model that predicts a ***Bernoulli probability distribution*** for each example.
- Popular Algorithms:
  - Logistic Regression
  - Naive Bayes
  - k-Nearest Neighbors
  - Decision Trees
  - Support Vector Machine


### 2. Multi-Class Classification:
- **Multi-class classification** refers to those classification tasks that have more than two class labels.
- **Multiclass classification** should not be confused with **multi-label classification**, where multiple labels are to be predicted for **each instance**.
- It makes the assumption that each sample is assigned to one and only one label: a fruit can be either an apple or a pear but not both at the same time.
- We can use ***OneVsRestClassifier***, ***OneVsOneClassifier***, ***OutputCoderClassifier*** for Multi-Class Classification.
- multi-class classification techniques can be categorized into following.

| Technique | Approach | Comments |
|-----------|----------|----------|
| Transformation to binary | **One-vs-Rest [OVR] (or) One-Against-All [OAA]** | It involves training a single classifier per class, with the samples of that class as positive samples and all other samples as negatives. <br />  This strategy requires the base classifiers to produce a real-valued confidence score for its decision. |
| Transformation to binary | **One-vs-One [OVO]** | It trains **K (K − 1) / 2** binary classifiers for a **K**-way multiclass problem. <br />  Each receives the samples of a pair of classes from the original training set, and must learn to distinguish these two classes. <br /> At prediction time, a voting scheme is applied: all **K (K − 1) / 2** classifiers are applied to an unseen sample and the class that got the highest number of "+1" predictions gets predicted by the combined classifier. |
| Extention from binary |  **NeuralNetworks <br /> D-Trees <br /> KNN </br> Naive Bayes <br /> SVM** | This section discusses strategies of extending the existing binary classifiers to solve multi-class classification problems. <br /> These types of techniques can also be called algorithm adaptation techniques.

### 3. Multi-Label Classification:


### 4. Imbalanced Classification:
- Imbalanced data typically refers to a problem with classification problems where the classes are not represented equally.
- ***ex:***
  - Consider Classification problem with 3 classes as Happy, Sad, Nuteral and data districution as below. This is an example of imbalanced dataset with ratio of **8:1:1**
    - Happy &rightarrow; **80%**
    - Sad &rightarrow; **10%**
    - Nuteral &rightarrow; **10%**
- **Note:**
  -  In case of imbalanced classes **confusion-matrix** is good technique to summarizing the performance of a classification algorithm.
  - **Precision-Recall** is a useful measure of success of prediction when the classes are very imbalanced.
    - **Precision** is a measure of the ability of a classification model to identify **only relevant data points**, 
    - **Recall** is a measure of the ability of a model to find **all the relevant cases** within a dataset.
    - The **precision-recall** curve shows the **trade-off** between precision and recall for **different threshold**. 
    - A high area under the curve represents both high recall and high precision, where **high precision** relates to a ***low false positive*** rate, and **high recall** relates to a ***low false negative rate***.

-  **How to Improve Performance of Imbalanced model:**
   -  Generally there are various techniques involved in improving the performance of imbalanced datasets.

| Method | Description | comment |
|--------|-------------|---------|
| **Under Sampling** | Remove samples from over-represented classes <br /> Use this if you have huge dataset | |
| **Over Sampling** | Add more samples from under-represented classes <br /> Use this if you have small dataset. | SMOTE |

- **SMOTE: Synthetic Minority Over-sampling Technique**
  - SMOTE is an over-sampling method.
  - It creates synthetic samples of the minority class.
  - Hint: **Use imblearn** class
- **Introduce Bias**
  - We can introduce some bias in our model minority classes, which will help in improving performance of the model while classifying various classes.
  - Hint: **Use sklearn.utils.class_weight** class

