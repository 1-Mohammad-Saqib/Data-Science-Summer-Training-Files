# Chapter 1 - Decision Tree

## 🎯 Objective

Understand the complete theory of Decision Trees including structure,
impurity measures, pruning, regression, and classification.

## 📚 Decision Tree

-   Supervised Machine Learning algorithm.
-   Used for Regression and Classification.
-   Makes predictions using Yes/No questions.

### Applications

-   Loan Approval
-   Disease Prediction
-   Fraud Detection
-   Customer Churn
-   Insurance Prediction

## 📚 Types of Machine Learning

### Supervised

-   Uses labeled data.
-   Input (X) and Output (Y) are known.

### Unsupervised

-   Uses unlabeled data.
-   Finds hidden patterns.

### Reinforcement

-   Learns using rewards and penalties.

## 📚 Components

-   Root Node: First node.
-   Parent Node: Creates child nodes.
-   Child Node: Created after splitting.
-   Decision Node: Asks questions.
-   Leaf Node: Final prediction.
-   Branch: Connection between nodes.
-   Splitting: Divides dataset.

## 📚 Entropy

-   Measures impurity (uncertainty).
-   Low entropy = Pure data.
-   High entropy = Mixed data.

## 📚 Information Gain

-   Reduction in entropy after splitting.
-   Information Gain = Entropy Before − Entropy After.
-   Highest Information Gain = Best Split.

## 📚 Gini Index

-   Measures impurity.
-   Lower Gini = Better Split.
-   Default criterion in DecisionTreeClassifier is `gini`.

## 📚 Underfitting

-   Model is too simple.
-   Fails to learn patterns.

## 📚 Overfitting

-   Model memorizes training data.
-   Performs poorly on new data.

## 📚 Pruning

-   Removes unnecessary branches.
-   Reduces overfitting.

### Pre-Pruning

-   max_depth
-   min_samples_split
-   min_samples_leaf

### Post-Pruning

Grow full tree then remove extra branches.

## 📚 Decision Tree Regression

-   Predicts continuous numerical values.
-   Uses `DecisionTreeRegressor()`.

Examples: - House Price - Salary - Insurance Charges

## 📚 Decision Tree Classification

-   Predicts categorical values.
-   Uses `DecisionTreeClassifier()`.

Examples: - Disease Prediction - Spam Detection - Loan Approval

## ⭐ Important Points

-   Decision Tree is supervised.
-   Entropy measures impurity.
-   Information Gain reduces entropy.
-   Lower Gini gives better split.
-   Overfitting memorizes data.
-   Underfitting learns too little.
-   Pruning removes extra branches.

## ❌ My Mistakes

-   Decision Tree is not only for Yes/No problems.
-   Entropy means impurity, not randomness.
-   Underfitting is not less data.
-   Overfitting is not more data.
-   Use Target Variable (Y), not Y-axis.

## ✅ Improvements

-   Say Continuous Numerical Values.
-   Say Categorical Values.
-   Mention Highest Information Gain.
-   Mention Lower Gini.

## 🎯 Viva Questions

1.  What is Decision Tree?
2.  What is Entropy?
3.  What is Information Gain?
4.  What is Gini Index?
5.  Difference between Overfitting and Underfitting?
6.  What is Pruning?
7.  Difference between DecisionTreeRegressor and DecisionTreeClassifier?

## 📝 One-Line Revision

-   Decision Tree → Supervised ML
-   Entropy → Impurity
-   Information Gain → Reduction in Entropy
-   Gini → Lower is Better
-   Underfitting → Too Simple
-   Overfitting → Memorizes
-   Pruning → Removes Extra Branches
-   DecisionTreeRegressor → Numerical Prediction
-   DecisionTreeClassifier → Categorical Prediction
