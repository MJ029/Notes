# Important Notes

### Durbin – Watson (DW) statistic:
- It must lie between 0 and 4.
- DW = 2, implies no autocorrelation.
- 0 < DW < 2 implies positive autocorrelation.
- 2 < DW < 4 indicates negative autocorrelation.

### VIF - Variance Influnce Factor:
- VIF <= 4 suggests no multicollinearity.
- VIF >= 10 implies serious multicollinearity.


### Residual vs Fitted Values Plots:
- It reveals various useful insights including outliers.
- The outliers in this plot are labeled by their observation number which make them easy to detect.
- There are two major things which you should learn:
  - If there exist any pattern (may be, a parabolic shape) in this plot, consider it as signs of non-linearity.
  - If a funnel shape is evident in the plot, consider it as the signs of non constant variance i.e. heteroskedasticity.
- Solution:
  - To overcome the issue of non-linearity, you can do a non linear transformation of predictors such as log (X), √X or X² transform the dependent variable.
  - To overcome heteroskedasticity, a possible way is to transform the response variable such as log(Y) or √Y. Also, you can use weighted least square method to tackle heteroskedasticity.

### Normal Q-Q Plot:
- The quantile-quantile is a scatter plot which helps us validate the assumption of normal distribution
- Using this plot we can infer if the data comes from a normal distribution. If yes, the plot would show fairly straight line.
-  Absence of normality in the errors can be seen with deviation in the straight line.
-  Solution:
   - If the errors are not normally distributed, non – linear transformation of the variables (response or predictors) can bring improvement in the model.

### Scale Location Plot:
- This plot is also used to detect homoskedasticity (assumption of equal variance).
- It shows how the residual are spread along the range of predictors. 
- It’s similar to residual vs fitted value plot except it uses standardized residual values.

### Residuals vs Leverage Plot:
- It is also known as Cook’s Distance plot. Cook’s distance attempts to identify the points which have more influence than other points.
- Such influential points tends to have a sizable impact of the regression line. In other words, adding or removing such points from the model can completely change the model statistics.
- Solution:
  - For influential observations which are nothing but outliers, if not many, you can remove those rows.
  - Alternatively, you can scale down the outlier observation with maximum value in data or else treat those values as missing values.