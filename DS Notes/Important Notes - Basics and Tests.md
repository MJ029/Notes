# Important Notes

### Durbin – Watson (DW) statistic:
- The Durbin Watson Test is a measure of **autocorrelation** (also called **serial correlation**) in **residuals** from ***regression*** analysis.
- Autocorrelation is the similarity of a time series over successive time intervals.
- It can lead to underestimates of the standard error and can cause you to think predictors are significant when they are not.
- The Durbin Watson test reports a test statistic, with a value from **0** to **4**.
  - DW = 2, implies no autocorrelation.
  - 0 < DW < 2 implies positive autocorrelation (common in time series data).
  - 2 < DW < 4 implies negative autocorrelation (less common in time series data).
- **Assumptions**:
  - That the **errors** are **normally distributed** with a mean of 0.
  - The **errors** are **stationary**.
  - A **rule of thumb** is that test statistic values in the range of 1.5 to 2.5 are relatively **normal**. Values outside of this range could be cause for concern.
### VIF - Variance inflation Factor:
- **variance inflation factor**(VIF) is a measure of the amount of multicollinearity in a set of multiple regression variables.
- A **variance inflation factor**(VIF) detects multicollinearity in regression analysis. it’s presence can adversely affect your regression results.
- The VIF estimates how much the variance of a regression coefficient is inflated due to multicollinearity in the model.
- VIFs are calculated by taking a predictor, and regressing it against every other predictor in the model. 
- Multicollinearity inflates the variance and **type II** error.
- Variance inflation factors range from 1 upwards.
  - VIF = 1 suggests no multicollinearity.
  - 1 < VIF < 5 suggests minimul multicollinearity.
  - 5 < VIF suggests serious multicollinearity.
- **Hints:**
  - High VIFs only exist in control variables, but not in variables of interest.
  - When a dummy variable that represents more than two categories has a high VIF, multicollinearity does not necessarily exist. 


### Residual vs Fitted Values Plots:
- It reveals various useful insights including outliers.
- The outliers in this plot are labeled by their observation number which make them easy to detect.
- There are two major things which you should learn:
  - If there exist any pattern (may be, a parabolic shape) in this plot, consider it as signs of non-linearity.
  - If a funnel shape is evident in the plot, consider it as the signs of non constant variance i.e. heteroskedasticity.
- **Solution:**
  - To overcome the issue of non-linearity, you can do a non linear transformation of predictors such as log (X), √X or X² transform the dependent variable.
  - To overcome heteroskedasticity, a possible way is to transform the response variable such as log(Y) or √Y. Also, you can use weighted least square method to tackle heteroskedasticity.

### Normal Q-Q Plot:
- The quantile-quantile is a scatter plot which helps us validate the assumption of **normal distribution**.
- Using this plot we can infer if the data comes from a normal distribution. If yes, the plot would show fairly straight line.
-  Absence of normality in the errors can be seen with deviation in the straight line.
-  **Solution:**
   - If the errors are not normally distributed, non – linear transformation of the variables (response or predictors) can bring improvement in the model.

### Scale Location Plot:
- This plot is also used to detect **homoskedasticity** (assumption of equal variance).
- It shows how the residual are spread along the range of predictors. 
- It’s similar to residual vs fitted value plot except it uses standardized residual values.

### Residuals vs Leverage Plot:
- It is also known as Cook’s Distance plot. Cook’s distance attempts to identify the points which have more influence than other points.
- Such **influential points** tends to have a sizable impact of the regression line. In other words, adding or removing such points from the model can completely change the model statistics.
- **Solution:**
  - For influential observations which are nothing but outliers, if not many, you can remove those rows.
  - Alternatively, you can scale down the outlier observation with maximum value in data or else treat those values as missing values.