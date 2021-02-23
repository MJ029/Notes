## Logistic Regression
- In statistics, the logistic model (or logit model) is used to <u>model the probability of a certain class or event existing such as</u> **pass/fail**, **win/lose**.
- Logistic regression is a statistical model that in its basic form uses a <u>*logistic*</u> function to model a **binary dependent** variable.
- The unit of measurement for the log-odds scale is called a logit, from logistic unit, hence the alternative names.
- Logistic regression can be **binomial**, **ordinal** or **multinomial**. Outputs with more than two values are modeled by multinomial logistic regression and, if the multiple categories are ordered, by ordinal logistic regression.
- The logistic regression model itself simply models probability of output in terms of input and does not perform statistical classification (it is not a classifier), though it can be used to make a classifier.

### Assumptions:
- The assumptions of linear regression are violated in Logistic Regression, some of them listed below.
  - The conditional distribution **y | x** is a ***Bernoulli*** distribution rather than a ***Gaussian*** distribution, because the dependent variable is binary.
  - The  **predicted values** are ***probabilities*** and are therefore restricted to *(0,1)* through the logistic distribution function because logistic regression predicts the probability of particular outcomes rather than the outcomes themselves.

### Maximum likelihood estimation:
- The regression **coefficients** are usually estimated using ***maximum likelihood estimation***.
- In machine learning applications where logistic regression is used for binary classification, the MLE minimises the Cross entropy loss function.
- In some instances, the model may not reach convergence. Non-convergence of a model indicates that the coefficients are not meaningful because the iterative process was unable to find appropriate solutions.
  - Having a <u>large ratio</u> of variables to cases results in an overly conservative Wald statistic and can lead to non-convergence. ***Regularized*** logistic regression is specifically intended to be used in this situation.
  - <u>Multicollinearity</u> refers to unacceptably high correlations between predictors. As multicollinearity increases, coefficients remain unbiased but standard errors increase and the likelihood of model convergence decreases.
  - <u>Sparseness</u> in the data refers to having a large proportion of empty cells (cells with zero counts). Zero cell counts are particularly problematic with categorical predictors.  With continuous predictors, the model can infer values for the zero cell counts, but this is not the case with categorical predictors. 
    - The model will not converge with zero cell counts for categorical predictors because the natural logarithm of zero is an undefined value so that the final solution to the model cannot be reached. 
    - To remedy this problem, researchers may collapse categories in a theoretically meaningful way or add a constant to all cells.
  - Another numerical problem that may lead to a lack of convergence is <u>complete separation</u>, which refers to the instance in which the predictors <u>perfectly predict</u> the criterion – all cases are accurately classified.
    -  In such instances, one should reexamine the data, as there is likely some kind of error.
   - One can also take semi-parametric or non-parametric approaches, e.g., via local-likelihood or nonparametric quasi-likelihood methods, which avoid assumptions of a parametric form for the index function and is robust to the choice of the link function