# Interview Questions Machine Learning

**What’s the trade-off between bias and variance? or What do you understand by Bias Variance trade off?**  
- Bias is error due to erroneous or overly simplistic assumptions in the learning algorithm you’re using.  
- This can lead to the model under-fitting your data, making it hard for it to have high predictive accuracy and for you to generalize your knowledge from the training set to the test set.  
- In other Words, Bias error is useful to quantify how much on an average are the predicted values different from the actual value.   
- A high bias error means we have a under-performing model which keeps on missing important trends.  
- Variance is error due to too much complexity in the learning algorithm you’re using.  
- This leads to the algorithm being highly sensitive to high degrees of variation in your training data, which can lead your model to over-fit the data.  
- You’ll be carrying too much noise from your training data for your model to be very useful for your test data.  
- In Other Words, Variance on the other side quantifies how are the prediction made on same observation different from each other.   
- A high variance model will over-fit on your training population and perform badly on any observation beyond training.  
- The bias-variance decomposition essentially decomposes the learning error from any algorithm by adding the bias, the variance and a bit of irreducible error due to noise in the underlying dataset.  
- Essentially, if you make the model more complex and add more variables, you’ll lose bias but gain some variance.  
- in order to get the optimally reduced amount of error, you’ll have to tradeoff bias and variance. You don’t want either high bias or high variance in your model.  
	
**Proper Definition**  
- The error emerging from any model can be broken down into three components mathematically.
		BiasVaianceTradeOff.png
		
**What is the difference between supervised and unsupervised machine learning?**  
**Supervised Learning:**  
- it requires training labeled data.  
- Ex: in order to do classification (a supervised learning task), you’ll need to first label the data you’ll use to train the model to classify data into your labeled groups.  
- in simple words, if you are training your machine learning task for every input with corresponding target, it is called supervised learning, which will be able to provide target for any new input after sufficient training.  
- Your learning algorithm seeks a function from inputs to the respective targets.  
- If the targets are expressed in some classes, it is called classification problem. 
- Alternatively, if the target space is continuous, it is called regression problem.
		
		
**Unsupervised learning:**  
- in contrast, does not require labeling data explicitly.  
- in Words, if you are training your machine learning task only with a set of inputs, it is called unsupervised learning, which will be able to find the structure or relationships between different inputs.  
- clustering is the most important unsupervised learning Algorithm, which will create different cluster of inputs and will be able to put any new input in appropriate cluster.  
- Few Unsupervised learning algorithms are:  
	- Anomaly detection  
	- Hebbian Learning  
	-  Latent variable models such as (Expectation–maximization algorithm,  Method of moments and etc...)  

	
**What’s a Fourier transform?**
- A Fourier transform is a generic method to decompose generic functions into a superposition of symmetric functions. 
- The Fourier transform finds the set of cycle speeds, amplitudes and phases to match any time signal. 
- A Fourier transform converts a signal from time to frequency domain — it’s a very common way to extract features from audio signals or other time series such as sensor data.
	
**What’s the difference between probability and likelihood?**

**Discrete Random Variables**
- Suppose that you have a stochastic process that takes discrete values (e.g., outcomes of tossing a coin 10 times, number of customers who arrive at a store in 10 minutes etc). 
- In such cases, we can calculate the probability of observing a particular set of outcomes by making suitable assumptions about the underlying stochastic process (e.g., probability of coin landing heads is p and that coin tosses are independent).
- Denote the observed outcomes by O and the set of parameters that describe the stochastic process as θ. 
- Thus, when we speak of probability we want to calculate P(O|θ). 
- In other words, given specific values for θ, P(O|θ) is the probability that we would observe the outcomes represented by O.
- However, when we model a real life stochastic process, we often do not know θ. 
- We simply observe O and the goal then is to arrive at an estimate for θ that would be a plausible choice given the observed outcomes O. 
- We know that given a value of θ the probability of observing O is P(O|θ). 
- Thus, a 'natural' estimation process is to choose that value of θ that would maximize the probability that we would actually observe O. 
- In other words, we find the parameter values θ that maximize the following function:
	L(θ|O)=P(O|θ)
- L(θ|O) is called the likelihood function. 
- Notice that by definition the likelihood function is conditioned on the observed O and that it is a function of the unknown parameters θ.

**Continuous Random Variables**
- In the continuous case the situation is similar with one important difference. 
- We can no longer talk about the probability that we observed O given θ because in the continuous case P(O|θ)=0. 
- Without getting into technicalities, the basic idea is as follows:
- Denote the probability density function (pdf) associated with the outcomes O as: f(O|θ). 
- Thus, in the continuous case we estimate θ given observed outcomes O by maximizing the following function:
	L(θ|O)=f(O|θ)
- In this situation, we cannot technically assert that we are finding the parameter value that maximizes the probability that we observe O as we maximize the PDF associated with the observed outcomes O.
	
**What is deep learning, and how does it contrast with other machine learning algorithms?**
- Deep learning is a subset of machine learning that is concerned with neural networks
- how to use backpropagation and certain principles from neuroscience to more accurately model large sets of unlabelled or semi-structured data.
- In that sense, deep learning represents an unsupervised learning algorithm that learns representations of data through the use of neural nets.
- Deep learning (also known as deep structured learning or hierarchical learning) is part of a broader family of machine learning methods based on learning data representations, as opposed to task-specific algorithms. Learning can be supervised, semi-supervised or unsupervised.
- Deep learning architectures such as deep neural networks, deep belief networks and recurrent neural networks have been applied to fields including computer vision, speech recognition, natural language processing, audio recognition, social network filtering, machine translation, bioinformatics and drug design, where they have produced results comparable to and in some cases superior to human experts.


**What is Ensemble learning ?**  
- **Ensemble methods** are meta-algorithms that combine several machine learning techniques into one predictive model in order to decrease variance (**bagging**), bias (**boosting**), or improve predictions (**stacking**).   
- **Ensemble learning** is the process by which multiple models, such as classifiers or experts, are strategically generated and combined to solve a particular computational intelligence problem.  
- Ensemble learning is primarily used to improve the performance of a model, or reduce the likelihood of an unfortunate selection of a poor one.  
- It can be used in 2 ways:  
	- Sequential:  
		- sequential ensemble methods where the base learners are generated sequentially.   
		- The overall performance can be boosted by weighing previously mislabeled examples with higher weight.  
		- The basic motivation of sequential methods is to exploit the dependence between the base learners.  
	- Parallel:  
		- parallel ensemble methods where the base learners are generated in parallel.   
		- The basic motivation of parallel methods is to exploit independence between the base learners since the error can be reduced dramatically by averaging.  
- Most ensemble methods use a single base learning algorithm to produce homogeneous base learners.  
- There are also some methods that use heterogeneous learners(Stacking)
- It can be categorized as below:  
	- Bagging  
	- Boosting  
	- Stacking.

