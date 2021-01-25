# REGRESSION - Important Points

- In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables/factors.
- It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors').
  - **Dependent variable:** The main factor that you’re trying to understand or predict.
  - **Independent variables:** The factors you suspect have an impact on your dependent variable.
- Regression analysis includes several variations, such as linear, multiple linear, and nonlinear. The most common models are simple linear and multiple linear. 
- Nonlinear regression analysis is commonly used for more complicated data sets in which the dependent and independent variables show a nonlinear relationship.

### Linear Regression:
#### Assumptions:
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

#### Rule of Thumb:
- Regression analysis requires at least **20 cases** (***samples size***) per independent variable in the analysis.
- It is important to check for **outliers** since linear regression is sensitive to outlier effects.

#### Notes:
- When the data is **not normally distributed** a non-linear transformation (e.g., log-transformation) might fix this issue.
- If multicollinearity is found in the data, **centering** the data (that is deducting the mean of the variable from each score) might help to solve the problem.  However, the simplest way to address the problem is to **remove** independent variables with high VIF values.
- If homoscedasticity is present, a non-linear correction might fix the problem.
- Check for **Influential cases** in dataset which also can affects the slope of a regression line.
- Generally, non-constant variance arises in presence of outliers or extreme leverage values. Look
- 
### 1. Simple Linear Regression:
- Simple linear regression is a statistical method that allows us to summarize and study relationships(trend) between two continuous (quantitative) variables.
- One variable, denoted **X**, is regarded as the **predictor**, **explanatory**, or **independent variable**.
- The other variable, denoted **y**, is regarded as the **response**, **outcome**, or **dependent variable**.

### Multi Linear Regression:
- Simple linear regression is a statistical method that allows us to summarize and study relationships(trend) between more than two continuous (quantitative) variables.
- One variable, denoted **X**, is regarded as the **predictor**, **explanatory**, or **independent variable**. In Multiple Linear model we will be having more than one variable.
- The other variable, denoted **y**, is regarded as the **response**, **outcome**, or **dependent variable**.
- Adding too many independent variables without any theoretical justification may result in an over-fit model.