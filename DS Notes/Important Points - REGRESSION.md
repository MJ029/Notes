# REGRESSION - Important Points

- In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables/factors.
- It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors').
  - **Dependent variable:** The main factor that you’re trying to understand or predict.
  - **Independent variables:** The factors you suspect have an impact on your dependent variable.
- Regression analysis includes several variations, such as linear, multiple linear, and nonlinear. The most common models are simple linear and multiple linear. 
- Nonlinear regression analysis is commonly used for more complicated data sets in which the dependent and independent variables show a nonlinear relationship.


## Linear Regression:
- Linear Regression is the process of estimating the relationships among variables/factors which are linear in nature. The Model is considered as linear when the relationship between **X** and **Y** is linear [***One of the main Assumptions of Linear model***].


### Assumptions:
- **Linearity:** 
  - The relationship between X and the mean of Y is **linear** & **additive**.
  - It can best be tested with **Scatter-plots**.
  - <del>Look for **residuals (errors) [vs] fitted values (predicted values) plots**</del>.

- **Homoscedasticity:** 
  - The **variance** of residual is the same for any value of X.
  - **Scatter-plot** is good way to check whether the data are homoscedastic.
  - The **Breusch-Pagan / Cook – Weisberg test or White general Test** is the ideal one to determine homoscedasticity. where **Goldfeld-Quandt** Test can also be used to test for heteroscedasticity.
  - Look for **residuals (errors) [vs] fitted values (predicted values) plots**. If heteroskedasticity exists, the plot would exhibit a funnel shape pattern

- **Autocorrelation:**
  - There is **little** or **no autocorrelation** in the data.
  - In other words when the value of y(x+1) is not independent from the value of y(x).
  - **Scatter-plot** allows you to check for autocorrelations
  - Test the linear regression model for autocorrelation with the **Durbin-Watson** test. 
  - Also, you can see **residual (vs) time plot** and look for the ***seasonal*** or ***correlated pattern*** in residual values.

- **Independence:** 
  - Observations (X) are **independent** of each other.
  - There is **little** or no **multicollinearity** in the data. Multicollinearity occurs when the independent variables are too highly correlated with each other.
  - It can ve tested through **Correlation matrix**, **Tolerance** & **Variance Inflation Factor** (VIF) 

- **Normality:** 
  - For any fixed value of X, Y is **normally distributed**.
  - It can best be checked with a **histogram** or a **Q-Q-Plot**.
  - Normality can be checked with a **goodness of fit test**, e.g., the Kolmogorov-Smirnov test.


### Rule of Thumb:
- Regression analysis requires at least **20 cases** (***samples size***) per independent variable in the analysis.
- It is important to check for **outliers** since linear regression is sensitive to outlier effects.


#### Notes:
- When the data is **not normally distributed** a non-linear transformation (e.g., log-transformation) might fix this issue.
- If multicollinearity is found in the data, **centering** the data (that is deducting the mean of the variable from each score) might help to solve the problem.  However, the simplest way to address the problem is to **remove** independent variables with high VIF values.
- If homoscedasticity is present, a non-linear correction might fix the problem.
- Check for **Influential cases** in dataset which also can affects the slope of a regression line.
- Generally, non-constant variance arises in presence of outliers or extreme leverage values. Look


### 1. Simple Linear Regression:
- Simple linear regression is a statistical method that allows us to summarize and study relationships(trend) between two continuous (quantitative) variables.
- One variable, denoted **X**, is regarded as the **predictor**, **explanatory**, or **independent variable**.
- The other variable, denoted **y**, is regarded as the **response**, **outcome**, or **dependent variable**.


### 2. Multi Linear Regression:
- Simple linear regression is a statistical method that allows us to summarize and study relationships(trend) between more than two continuous (quantitative) variables.
- One variable, denoted **X**, is regarded as the **predictor**, **explanatory**, or **independent variable**. In Multiple Linear model we will be having more than one variable.
- The other variable, denoted **y**, is regarded as the **response**, **outcome**, or **dependent variable**.
- Adding too many independent variables without any theoretical justification may result in an over-fit model.


### 3. Polynomial Regression:
-  **polynomial regression** is a form of regression analysis in which the relationship between the independent variable x and the dependent variable y is modelled as an **n'th** degree polynomial in x.
-  It fits a **nonlinear relationship** between the value of **X** and the corresponding conditional ***mean*** of **y**.
- Although polynomial regression fits a **nonlinear** model to the data, as a statistical estimation problem it is **linear**.
-  It is considered to be a **special** case of **multiple linear regression**.
-  This model try's to fit the best fit model which is not **under-fitting** and **Over-Fiting**.
- It is highly sensitive to **Outliers**. Presence of one or two outliers in the data can seriously affect the results of the nonlinear analysis.
- <u>**Tuning Parameters:**</u>
  - degree:
    - The degree of the polynomial features. ***Default*** to 2.


### 4. Lasso Regression: [**L**east **A**bsolute **S**hrinkage **S**elector **O**perator]
- It is a type of linear regression model which uses **Shrinkage**. 
- **Shrinkage** is the point where values are shrunk towards a central point similar to ***mean***.
- It procedure encourages simple, sparse models (i.e. models with fewer parameters).
- This model is **well-suited** for models showing high levels of ***muticollinearity*** or when you want to automate certain parts of model selection.
- It is similar to ***stepwise selection***.
- It performs **L1 Regularization** which adds a **penalty** equal to the ***absolute value*** of the ***magnitude*** of coefficients.
- <u>**Tuning Parameters:**</u>
  - lambda(**λ**):
    - It controls the ***strength*** of the L1 penalty (**or**)  basically the ***amount of shrinkage***.
    - When **λ** == 0 --> no parameters are eliminated. 
    - When **λ** == ∞ --> all coefficients are eliminated.
    - **Variance** < **λ** < **Bias**


### 5. Ridge Regression
- **Ridge regression** is a way to create a ***parsimonious*** model when the number of **predictor variables** in a set **exceeds** the number of **observations**, or when a data set has ***multicollinearity*** (correlations between predictor variables).
- It is Similar to ***Tikhivov’s method***.
- While least squares produces ***unbiased estimates***, **variances** can be so large that they may be wholly **inaccurate**. Ridge regression **adds** just enough **bias** to make the estimates reasonably reliable approximations to true population values.
- This model is well suited for models tend to over-fitting. It generally reduces overfitting.
- It performs **L2 Regularization** which adds a **penalty** equal to the ***square value*** of the magnitude of coefficients. This is equivalent to saying **minimizing** the cost function.
- All coefficients are shrunk by the same factor, so none are eliminated. Unlike **L1 regularization**, It will not result in ***sparse models***.
- <u>**Tuning Parameters:**</u>
  - lambda(**λ**):
    - It controls the ***strength*** of the L1 penalty (**or**)  basically the ***amount of shrinkage***.
    - When **λ** == 0 --> equals least squares regression. 
    - When **λ** == ∞ --> all coefficients are shrunk to zero.
    - <del>**Variance** < **λ** < **Bias**</del>


### 6. Gradient Descent:
- **TODO:** Need to put right content Here


## Non Linear Regression
- **Nonlinear** regression is a form of regression analysis in which observational data are modeled by a function which is a **nonlinear combination of the model parameters** and depends on one or more independent variables.
- <u>**Equation:**</u>  
  - **Y = f(X, β) + ε**   
 
<center>

| Parameter | Description |  
| :---------: | :-----------: |  
| X | Vector Of *p* Predictors. |  
| β | Vector o *k* parameters. |  
| f(-) | Regressor Functions. |  
| ε | Error Term. |

</center>

### Assumptions:
- **TODO:** Need to work on Assumptions of NLR.


### 1. Support Vector Regression:
- Support Vector Regression [SVR] is a *nonlinear generalization* of the **Generalized Portrait** algorithm, it is firmly grounded in the framework of ***statistical learning theory***, or ***VC theory***.
- Our goal is to find a function **f(*x*)** that has at most ***ε*** deviation from the actually obtained targets **y** for all the training data, and at the same time is as flat as possible.
- Our objective, when we are moving on with **SVR**, is to basically consider the points that are within the decision boundary line.
- It is considered a ***non parametric technique*** because it **relies** on **kernel** functions.
- In other words, we do not care about errors as long as they are less than ***ε***, but will not accept any deviation larger than ***ε***.
- <u>**Hyper-Parameters:**</u>
  - <u>Kernal:</u>
    - Maps **lower** dimentional data into a **higher** dimentional data.
    - Generally it could be ***linear***, ***polynomial***, ***sigmoid*** & ***rbf***.
    - Changing Kernal is known as ***kernal Trick***.
    - **Note:**
      - A kernel helps us find a hyperplane in the higher dimensional space without increasing the computational cost. Usually, the computational cost will increase if the dimension of the data increases.

  - <u>Support Vectors:</u>
    - Actual **data-points** which are close to ***line of boundary***.
  
  - <u>Hyper Plane:</u>
    - Is **SVM** It is the important factor which separates the data classes, on we can say it the line between data classes.
    - In **SVR**, Hyper Plane will play the same role as SVM, but as we discussed before the key change is, here it is a line between linear(continuous) data.
  
  - <u>Boundary Plane (**or**) Decision Boundary (**margin of tolerance**):</u>
    - It is defining the **upper/lower** boundaries from the Hyper-Plane.
    - It act as a **margin** between Hyper-Plane and data points.
    - The distance between Boundary-Plane and Hyper-Plane are considered as **epsilon (*ε*)** distance. So the lines that we draw are at *‘+ε’* and *‘-ε ’* distance from Hyper Plane.

  - <u>C - Regularization Parameter:</u>
    - The C parameter tells the SVM/SVR optimization how much you want to avoid misclassifying each training example.
    - When the C parameter is set to infinite, The optimal hyperplane (if exists) will be the one that completely separates the data.
    - At such a high level of misclassification penalty, soft margin will not hold existence as there will be no room for error.
    - Conversely, a very small value of C will cause the optimizer to look for a larger-margin separating hyperplane, even if that hyperplane misclassifies more points.
    -  For very tiny values of C, you should get misclassified examples, often even if your training data is linearly separable.
  
  - <u>Gama:</u>
    - The gamma parameter in SVM tuning signifies the influence of points either near or far away from the hyperplane.
    - If GAMA is low:
      - The model will be too constrained and include all points of the training dataset, without really capturing the shape.
    - If GAMA is high:
      - The model will capture the shape of the dataset well.

  - **Notes:**
    - The minimum time complexity for training an SVM is **O(n2)**. According to this fact, we can train Large datasets in SVM.
    - Remaining things related to SVM/SVR can be seen in [More](../Interview%20Questions/../Interview%20Questions/Interview%20Questions%20-%20Support%20Vector%20Machine.md)
- **TODO:** Still Yet to get more info on How to Choose Right Kernal for our model.

### 2. Decision Tree Regression:
- Decision tree builds ***Classification*** or ***Regression*** models in the form of a **tree** structure. It breaks down a data-set into smaller subsets while at the same time an associated decision tree is incrementally developed.
- D-Tree is one of the predictive modeling approaches used in statistics, data mining and machine learning.
- D-Tree has 3 main components:

| Component | Description |
|-----------|-------------|
| Root Node | It is considered to be the Best predictor which placed as topmost node in tree. |
| Decision Node | It is considered to be the intermediate nodes which is derived from root node or other Decision nodes.<br /> A Decision Node has two or more branches which holds attributes(IV's) or leaf nodes|
| Leaf Node | It represents a classification or decision (DV). |

#### Types of Decision Tree:

| Type | Description | Comments |
|------|-------------|----------|
| ID3 | Iterative Dichotomiser 3 | It can be used in both Regression and Classification tasks. <br /> When it is used in **Regression** it uses ***Standard Deviation Reduction*** technique to solve the problem. <br /> When it is used in **Classification** it uses ***Entropy and Information Gain*** techniques to solve the problem.|
| C4.5 (or) J4.8 | successor of ID3 | It can be used only for **Classification** problem, It uses ***Information Gain Ratio*** technique to solve the problem. |
| CART | Classification And Regression Tree | It can be used only for **Classification** problem, It uses ***Gini Index*** technique to solve the problem. |
| CHAID | Chi-square automatic interaction detection | |
| MARS | extends decision trees to handle numerical data better | |
| Conditional Inference Trees | | Statistics-based approach that uses non-parametric tests as splitting criteria, corrected for multiple testing to avoid overfitting.<br /> This approach results in unbiased predictor selection and does not require pruning.|

- ***Overfitting*** is one of the problem we will encounter in most of the machine learning models is a significant practical difficulty for **D-Trees** and other predictive algorithms.
- In simple, "*Overfitting is a modeling error which occurs when a function is too closely fit to a limited set of data points*".
- In statistics, *"The production of an analysis that corresponds too closely or exactly to a particular set of data, and may therefore fail to fit additional data or predict future observations reliably"*.

#### Workflow:
<p align="center">
  <img src="draw%20files/D-Tree/ID3-Regression.png">
</p>


#### Note:
- **Decision List** is one special type of decision tree algorithm available which is a *one-sided decision tree*, so that every internal node has exactly 1 leaf node and exactly 1 internal node as a child (except for the bottom-most node, whose only child is a single leaf node).
- Concepts like **Pre-Pruning** and **Post-Pruning** will help us to avoid overfitting in building decision trees.
- **Pre-Pruning**:
  - Stop growing the tree earlier, before it perfectly classifies the training set.
- **Post-Pruning**:
  - Allows the tree to perfectly classify the training set, and then post prune the tree.
  - Practically This approach gives us better result compare to Pre-Pruning, because it is not easy to precisely estimate when to stop growing the tree.
- Some techniques, often called ensemble methods will construct more than one decision tree as follows
  - <u>**AdaBoost:**</u>
    - This method is a subset of ***Boosted Tree*** algorithms.
    - Incrementally building an ensemble by training each new instance to emphasize the training instances previously mis-modeled.
    - This can be used for regression-type and classification-type problems.
  - <u>**Random Forest:**</u>
    - This is also known as ***Bagged Decision**8 Tree or ***Bootstrap Aggregated Tree***.
    - This is one of the early ensemble method, builds multiple decision trees by repeatedly resampling training data with replacement, and voting the trees for a consensus prediction.
  - <u>**PCA: Principal Component Analysis**</u>
    - This is also known as ***Rotation Tree***.
    - Every decision tree is trained by first applying principal component analysis (PCA) on a random subset of the input features.

### 3. Random Forest Regression:
- **TODO:** Need to work.


## Evaluation Metrics:
- **TODO:** Need to work on Assumptions of Metrics.