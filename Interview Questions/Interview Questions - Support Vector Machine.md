# Support Vector Machine Important points

### Hint:
- hard margin is known to be, The SVM allows very low error in classification.
- The minimum time complexity for training an SVM is O(n2). According to this fact, we can train Large datasets in SVM.
- Datasets which have a clear classification boundary will function best with SVM’s.
- The effectiveness of SVM dependes on below.
	- Kernal Trick (Kernal selection)
	- Kernal Parameters
	- Soft Margin Parameter(C)
- Support vectors are the data points that lie closest to the decision surface.
- When we are using RBF kernel in SVM with high Gamma value, The model would consider only the points close to the hyperplane for modeling.
	
### 1) What happend when C paramter in set to infinite ?
- When the C parameter is set to infinite, The optimal hyperplane (if exists) will be the one that completely separates the data.
- At such a high level of misclassification penalty, soft margin will not hold existence as there will be no room for error.
- It is recommended to Keep Values of C between 0.1 < c < 100.

### 2) What is Hard-Margin ?
- A hard margin means that an SVM is very rigid in classification and tries to work extremely well in the training set, causing overfitting.

### 3) What is the use of Gama Parameter(decision boundary) in SVM.
- The gamma parameter in SVM tuning signifies the influence of points either near or far away from the hyperplane.
- If GAMA is low:
	The model will be too constrained and include all points of the training dataset, without really capturing the shape.
- If GAMA is high:
	The model will capture the shape of the dataset well.
- It is recommended to Keep Values of GAMMA between 0.0001 < gamma < 10
		
### 4) How do I select SVM kernels?
- The only way to choose the best kernel is to actually try out all possible kernels, and choose the one that does the best empirically.

### 5) differences between various kernel functions.
- **Translation invariance:**
  - RBF kernel is the only kernel out of the above that is translation invariant.

- **Inner product vs Euclidean distance:**
  -  Related to the above point, RBF kernel is a function of the Euclidean distance between the points, whereas all other kernels are functions of inner product of the points.
  - Again, it makes more intuitive sense to have Euclidean distance — points that are closer should be more similar.
- **Normalized:**
  - A kernel is said to be normalized if  **K(x,x)=1**  for all  **x** .
  -  This is true for only RBF kernel.



## Important Questions

### Translation Invariance
- **Translation Invariance** (or) **Translational symmetry** is a property of a mathematical object (or a class of mathematical objects) which remains unchanged if we move it from one place to another without rotating it.
- **Pooling** in CNN is one of the best example of Transation Invariant