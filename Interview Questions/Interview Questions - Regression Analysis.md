# Regression Analysis Important points

### Hints:
- Linear relationship between the dependent and independent variable
- Independent variables in the dataset should not exhibit any <u>multicollinearity</u>.
- There should be an <u>equal distribution of errors</u>(Homoscedasticity).
- Remember formulas of RMSE / MSE / MAE
- Q-Q plots
- curse of dimensionality
- The mean of residuals is always equal to Zero, coz the sum of the residuals in regression is always equal to Zero.
- Thus, it implies that the mean will also be Zero if the sum of the residuals is Zero.
- Heteroscedasticity in Linear regression will have different error terms(variance).
- Homoscedasticity in Linear regression will have equal error terms(variance).
- In SLR we need to evaluate 2 Co-efficient [y = mx + b]
- Correlation coefficient always range is between [-1 ,1]
- When training a linear regression model, Over-fitting is more likely if we have less data
- We can also compute the coefficient of linear regression with the help of an analytical method called “Normal Equation”. 
- If two variables are correlated, It is not necessary that they have a linear relationship
- Correlated variables can have zero correlation coefficient.
- The relationship is symmetric between x and y in case of correlation but in case of regression it is not symmetric.
- we cannot calculate the skewness of variables based on mean and median.
- The Lasso does not admit a closed-form solution. The L1-penalty makes the solution non-linear. So we need to approximate the solution.

	
**Assumptions in linear regression**  
- linearity separable  
- Independent variable have restricted multicollinearity.  
- Homoscedasticity

**What is the generalized linear model?**  
- The generalized linear model is the derivative of the ordinary linear regression model.  
- GLM is more flexible in terms of residuals and can be used where linear regression does not seem appropriate.  
- GLM allows the distribution of residuals to be other than a normal distribution.  
- It generalizes the linear regression by allowing the linear model to link to the target variable using the linking function.  
- Model estimation is done using the method of maximum likelihood estimation.  
	
**What is Diff between R2 and Adj-R2 ?**  
- Both of these values used for model validation  
- R square accounts for the variation of all independent variables on the dependent variable.  
- One drawback of R2 is that it will always increase with the addition of a new feature, whether the new feature is useful or not.  
- In other words, it considers each independent variable for explaining the variation.  
- Adjusted R square, it accounts for the significant variables alone for indicating the percentage of variation in the model.  
- The adjusted R2 overcomes this drawback. The value of the adjusted R2 increases only if the newly added feature plays a significant role in the model.  
- By significant, we refer to the P values less than 0.05.  

**What is RMSE and MSE ?**  
- The most common measures of accuracy for any linear regression are RMSE and MSE.  
- MSE stands for Mean Square Error  
- RMSE stands for Root Mean Square Error.  
- <<Formula for RMSE and MSE>>  
	
**What is the use of Regularization ?**  
- Regularization is a technique that is used to avoid the problem of over-fitting the model.  
- When a very complex model is implemented on the training data, it over-fits.  
- At times, the simple model might not be able to generalize the data and the complex model over-fits.  
- To address this problem, regularization is used.  
- Regularization is nothing but adding the coefficient terms (betas) to the cost function so that the terms are penalized and are small in magnitude.  
- This essentially helps in capturing the trends in the data and at the same time prevents over-fitting by not letting the model become too complex.  
	
**Explain L1 and L2 Regularization ?**  
- L1 Regularization:
	- It is known as L1 or *LASSO* regularization.  
	- Here, the *absolute values of the coefficients* are added to the cost function.   
	- This regularization technique gives sparse results, which lead to *feature selection* as well.  
- L2 Regularization:
	- It is known as L2 or *Ridge* regularization.  
	- Here, the *squares of the coefficients* are added to the cost function.  
	- When lambda is 0, model works like linear regression model.  
	- When lambda goes to infinity, we get very, very small coefficients approaching 0.  

**Explain the bias-variance trade-off ?**  
- Bias:  
	- the difference between the values predicted by the model and the real values.  
	- It is considered as an error.  
	- goals of an ML algorithm is to have a low bias.  
- Variance:  
	- The sensitivity of the model to small fluctuations in the training data-set.  
	- goal of an ML algorithm is to have low variance.  
	- For a data-set that is not exactly linear, it is not possible to have both bias and variance low at the same time.
	- A straight line model will have low variance but high bias  
	- high-degree polynomial will have low bias but high variance  
	- There is no escaping the relationship between bias and variance in machine learning.  
		- Decreasing the bias increases the variance.  
		- Decreasing the variance increases the bias.  

**What is Generalization error ?**  
- Generalization error in statistics is generally the out-of-sample error which is the measure of how accurately a model can predict values for previously unseen data.  
- In simpe, The error rate in test set is known as generalization error. when you are training your model in training set and testig it using test set.

**How does multicollinearity affect the linear regression ?**  
- Multicollinearity occurs when some of the independent variables are highly correlated (positively or negatively) with each other.  
- This multicollinearity causes a problem as it is against the basic assumption of linear regression.  
- The presence of multicollinearity does not affect the predictive capability of the model.   
- So, if you just want predictions, the presence of multicollinearity does not affect your output.  
- However, if you want to draw some insights from the model and apply them in, let’s say, some business model, it may cause problems.  
- One of the major problems caused by multicollinearity is that it leads to incorrect interpretations and provides wrong insights.  
- A highly effective way of dealing with multicollinearity is the use of VIF (Variance Inflation Factor).  
- Higher the value of VIF for a feature, more linearly correlated is that feature.  
- Simply remove the feature with very high VIF value and re-train the model on the remaining data-set to get more accurate results.  

**What is VIF ? how to calculate ?**  
- Variance Inflation Factor (VIF) is used to check the presence of multicollinearity in a data-set.  
- Multicollinearity is when there’s correlation between predictors (i.e. independent variables) in a model
- it’s presence can adversely affect your regression results.   
- The VIF estimates how much the variance of a regression coefficient is inflated due to multicollinearity in the model.  
- VIFs are calculated by taking a predictor, and regressing it against every other predictor in the model. This gives you the R-squared values, 
which can then be plugged into the VIF formula.   
- formula = 1/1-Ri^2  
- A rule of thumb for interpreting the variance inflation factor  
	- 1 = not correlated.  
	- Between 1 and 5 = moderately correlated.  
	- Greater than 5 = highly correlated.  
		
**How can you avoid the over-fitting of your model?**  
- Keep the model simple:   
	take fewer variables into account, thereby removing some of the noise in the training data  
- Use cross-validation techniques, such as k folds cross-validation   
- Use regularization techniques, such as LASSO, that penalize certain model parameters if they're likely to cause over-fitting  

**What are the feature selection methods used to select the right variables?**  
- Filter Methods:  
	- Linear discrimination analysis  
	- ANOVA  
	- Chi-Square  
- Wrapper Methods:  
	- Forward Selection  
	- Backward Selection  
	- Recursive Feature Elimination  

**What is Curse of dimentionality ?**   

**What is the need of dimensionality reduction ?**  
- Dimensionality reduction refers to the process of converting a data set with vast dimensions into data with fewer dimensions (fields) to convey similar information concisely.   
- This reduction helps in compressing data and reducing storage space.  
- It also reduces computation time as fewer dimensions lead to less computing.   
- It removes redundant features; for example, there's no point in storing a value in two different units (meters and inches).   
	
**What is Homoscedasticity ?**  
- It ensures that the error terms are equally distributed.  
- It is one of the thumb assumption of Linear regression model.  
	
**What is Heteroscedasticity ?**  
- It is inverse to Homoscedasticity.  
- It entails that there is no equal distribution of the error terms.  
- You use a log function to rectify this phenomenon.  
- The presence of heteroscedasticity can often be seen in the form of a cone-like scatter plot for residual vs fitted values.  

**How to avoid Heteroscedasticity problem ?**  
- There are some ways that may lead to a reduction of heteroscedasticity.  
- Logarithmic the data:  
	- A series that is increasing exponentially often results in increased variability.  
	- This can be overcome using the log transformation.  
- Using weighted linear regression:  
	- Here, the OLS method is applied to the weighted values of X and Y.  
	- One way is to attach weights directly related to the magnitude of the dependent variable.  
	
**How do you interpret the residual vs fitted value curve?**  
- The residual vs fitted value plot is used to see whether the predicted values and residuals have a correlation or not.  
- If the residuals are distributed normally, with a mean around the fitted value and a constant variance, our model is working fine  
- otherwise, there is some issue with the model.  
- The most common problem that can be found when training the model over a large range of a data-set is heteroscedasticity  
- The presence of heteroscedasticity can be easily seen by plotting the residual vs fitted value curve.  

**What is Outlier ?**  
- An Outlier is an observation point distant from other observations.  
- It might be due to a variance in the measurement.   
- It can also indicate an experimental error.  
- Under such circumstances, you need to exclude the same from the data set.  

**How to handle Outlier in data-set ?**  
- There is no strict mathematical calculation of how to determine an outliner.   
- Deciding whether an observation is an outlier or not, is itself a subjective exercise.  
- However, you can detect outliers through various methods.   
- some of'em are graphical also known as "normal probability plots", whereas some are model-based.  
- You have some hybrid techniques such as Boxplots.  
- This is known as "The Outliner Treatment"  
- Some of the methods of eliminating outliers are the "Z-Score" and the "IQR Score" methods.  
- Try normalizing the data. This way, the extreme data points are pulled to a similar range.  
	
**How to improve performance of a Regression models**  
- The Outliner Treatment:  
	- Outlier have great significance in linear regression because regression is very sensitive to Outlier.  
	- Therefore, it becomes critical to treat Outlier with appropriate values.  
	- It can also prove useful if you replace the values with MEAN, MEDIAN, MODE (or) PERCENTILE depends on distribution.  
	- Some of the methods of eliminating Outlier are the "Z-Score" and the "IQR Score" methods.  

**Cons of Regression Analysis:**  
- One of the Cons of Regression analysis is that is sensitive and dependent on outliner.  
- another notable problem in Machine learning is Under-fitting/Over-fitting.  
	
**What is feature engineering ?**  
- Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.  
- In layman terms, feature engineering means the development of new features that may help you understand and model the problem in a better way.  
- It works on 2 ways:  
	- Business driven:  
		- It revolves around the inclusion of features from a business point of view.  
		- The job here is to transform the business variables into features of the problem.  
	- data driven:  
		- In case of data-driven feature engineering, the features you add do not have any significant physical interpretation,   
		but they help the model in the prediction of the target variable.  

**What is Gradient descent and When to use Gradient descent ?**  
- Gradient descent is an optimization algorithm.  
- In linear regression, it is used to optimize the cost function and find the values of the βs (estimators) corresponding to the optimized value of the cost function.  
- Needs hyper-parameter tuning for alpha (learning parameter)  
- It is an iterative process  
- O(kn2) time complexity  
- Preferred when n is extremely large  
- Note:   
		- ‘k’ is the maximum number of iterations for gradient descent  
		- ‘n’ is the total number of data points in the training set.

**How to choose the value of the parameter learning rate (α)?**  
- Selecting the value of learning rate is a tricky business.  
	- If the value is too small, the gradient descent algorithm takes ages to converge to the optimal solution.
	- If the value of the learning rate is high, the gradient descent will overshoot the optimal solution and most likely never converge to the optimal solution.  
- To overcome this problem, you can try different values of alpha over a range of values and plot the cost vs the number of iterations.  
- Then, based on the graphs, the value corresponding to the graph showing the rapid decrease can be chosen. 
	
**How to choose the value of the regularization parameter (λ)?**  
- Selecting the regularization parameter is a tricky business.  
	- If the value of λ is too high, it will lead to extremely small values of the regression coefficient β, which will lead to the model under-fitting (high bias – low variance).   
	- If the value of λ is 0 (very small), the model will tend to over-fit the training data (low bias – high variance).  
- There is no proper way to select the value of λ.  
- we can use concept like PCA or LDA to identify the optimized value for this parameter with sub-sampling data-set.  
		
**Why not to use linear regression for time series analysis?**  
- One can use linear regression for time series analysis, but the results are not promising.  
- So, it is generally not advisable to do so. The reasons behind this are Time series data is mostly used for the prediction of the future, but linear regression seldom gives good results for future prediction as it is not meant for extrapolation.  
- Mostly, time series data have a pattern, such as during peak hours, festive seasons, etc.,   
- which would most likely be treated as Outlier in the linear regression analysis.  

**What value is the sum of the residuals of a linear regression close to Justify ?**  
- The sum of the residuals of a linear regression is 0.  
- Linear regression works on the assumption that the errors (residuals) are normally distributed with a mean of 0 and variance 1.  
- Formula:  
	Y = βT X + ε  

	Y --> target or dependent variable.  
	β --> vector of the regression coefficient.  
	X --> feature matrix containing all the features as the columns.  
	ε --> residual term such that ε ~ N(μ,σ2).  
Note: N(μ,σ2) is the standard notation for a normal distribution having mean μ and standard deviation σ2.  

**What is the reason behind the beta value for a certain variable varies wildly when You run your regression on different subsets of your data.**  
- This is due to that the dataset is heterogeneous.  
- To overcome this problem, the dataset should be clustered into different subsets, and then separate models should be built for each cluster.   
- Another way to deal with this problem is to use non-parametric models, such as decision trees, which can deal with heterogeneous data quite efficiently.  
	
**What is the reason behind that there is an infinite number of best estimates for the regression coefficients.**  
- This arises when there is a perfect correlation (positive or negative) between some variables.  
- In this case, there is no unique value for the coefficients, and hence, the given condition arises.  
	
**How is hypothesis testing used in linear regression?**  
- Hypothesis testing can be carried out in linear regression for the following purposes  
	- To check whether a predictor is significant for the prediction of the target variable.  
	- Two common methods are used:  
		- By the use of p-values  
			- If the p-value of a variable is greater than a significant level (usually 0.05), the variable is insignificant in the prediction of the target variable.  
		- By checking the values of the regression coefficient  
			- If the value of regression coefficient corresponding to a predictor is zero  
			- that variable is insignificant in the prediction of the target variable and has no linear relationship with it.  
	- To check whether the calculated regression coefficients are good estimators of the actual coefficients.    

**Which graphs are suggested to be observed before model fitting ?**  
- Before fitting the model, one must be well aware of the data, such as what the trends, distribution, skewness, etc.   
- Graphs such as histograms, box plots, and dot plots can be used to observe the distribution of the variables.
- Apart from this, one must also analyze what the relationship between dependent and independent variables is. This can be done by scatter plots, rotating plots, dynamic plots, etc.  
	
**What is the difference between stochastic gradient descent (SGD) and gradient descent (GD)?**  
- Both algorithms are methods for finding a set of parameters that minimize a loss function by evaluating parameters against data and then making adjustments.  
- In standard gradient descent, you'll evaluate all training samples for each set of parameters.  
- In stochastic gradient descent, you'll evaluate only 1 training sample for the set of parameters before updating them.   
	
**When to use GD and SGD ?**  
- GD theoretically minimizes the error function better than SGD.  
- However, SGD converges much faster once the data-set becomes large.  
- That means GD is preferable for small data-sets while SGD is preferable for larger ones.  
- however, SGD is used for most applications because it minimizes the error function well enough while being much faster and more memory efficient for large data-sets.  
	
