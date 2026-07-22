# Chapter 2 - Random Forest

## 🎯 Objective

Understand Random Forest, Bootstrap Sampling, Bagging, Voting, Random
Forest Regressor, and Random Forest Classifier.

------------------------------------------------------------------------

# 📚 1. Random Forest

-   Random Forest is a **Supervised Machine Learning algorithm**.
-   It is made up of **multiple Decision Trees**.
-   Used for both Regression and Classification.
-   Gives more accurate predictions than a single Decision Tree.

### Why Random Forest?

-   Reduces overfitting.
-   Improves accuracy.
-   More robust than a single Decision Tree.

------------------------------------------------------------------------

# 📚 2. Bootstrap Sampling

-   Creates multiple datasets from the original dataset.
-   Uses **sampling with replacement**.
-   The same row can appear multiple times.
-   Helps create different Decision Trees.

------------------------------------------------------------------------

# 📚 3. Bagging (Bootstrap Aggregating)

-   Trains multiple Decision Trees using bootstrap samples.
-   Combines predictions from all trees.
-   Reduces variance and overfitting.

------------------------------------------------------------------------

# 📚 4. Voting

## Classification

-   Each tree predicts a class.
-   Final prediction = **Majority Vote**.

Example: - Yes, No, Yes, Yes → Final = Yes

## Regression

-   Each tree predicts a number.
-   Final prediction = **Average** of all predictions.

Example: - 5000, 5200, 5100 → Final = 5100

------------------------------------------------------------------------

# 📚 5. Random Forest Regressor

-   Supervised Regression algorithm.
-   Predicts **continuous numerical values**.
-   Uses multiple Decision Trees.
-   Final prediction = Average.

Examples: - House Price Prediction - Salary Prediction - Insurance
Charges Prediction

Algorithm:

``` python
from sklearn.ensemble import RandomForestRegressor
```

------------------------------------------------------------------------

# 📚 6. Random Forest Classifier

-   Supervised Classification algorithm.
-   Predicts **categorical values**.
-   Uses multiple Decision Trees.
-   Final prediction = Majority Vote.

Examples: - Disease Prediction - Loan Approval - Spam Detection - Fraud
Detection

Algorithm:

``` python
from sklearn.ensemble import RandomForestClassifier
```

------------------------------------------------------------------------

# 📊 Comparison

  Decision Tree      Random Forest
  ------------------ ------------------
  One Tree           Multiple Trees
  Faster             Slightly Slower
  More Overfitting   Less Overfitting
  Lower Accuracy     Higher Accuracy

  RandomForestRegressor   RandomForestClassifier
  ----------------------- ------------------------
  Continuous Output       Categorical Output
  Average Prediction      Majority Voting

------------------------------------------------------------------------

# ⭐ Important Points

-   Random Forest uses multiple Decision Trees.
-   Bootstrap Sampling creates different datasets.
-   Sampling is done **with replacement**.
-   Bagging combines multiple Decision Trees.
-   Regression uses Average.
-   Classification uses Majority Vote.
-   Random Forest reduces overfitting.

------------------------------------------------------------------------

# ❌ My Mistakes

-   Thought Random Forest always uses average (it uses average only for
    regression).
-   Used "Y-axis" instead of "Target Variable (Y)".
-   Forgot that Classification uses majority voting.

------------------------------------------------------------------------

# ✅ Improvements

-   Choose algorithm based on Target Variable (Y).
-   Continuous Target → RandomForestRegressor.
-   Categorical Target → RandomForestClassifier.
-   Remember Bootstrap ≠ Bagging.
-   Remember Majority Vote for Classification.

------------------------------------------------------------------------

# 🎯 Viva Questions

1.  What is Random Forest?
2.  Why is it called Random Forest?
3.  Why is Random Forest better than Decision Tree?
4.  What is Bootstrap Sampling?
5.  What is Bagging?
6.  What is Voting?
7.  How does Random Forest predict in Regression?
8.  How does Random Forest predict in Classification?
9.  What is RandomForestRegressor?
10. What is RandomForestClassifier?

------------------------------------------------------------------------

# 💼 Interview Questions

-   Difference between Decision Tree and Random Forest.
-   What is Bootstrap Sampling?
-   What is Bagging?
-   Why does Random Forest reduce overfitting?
-   Difference between RandomForestRegressor and RandomForestClassifier.

------------------------------------------------------------------------

# 🧠 Memory Tricks

-   Random Forest → Many Decision Trees.
-   Bootstrap → Different datasets.
-   Bagging → Train many trees.
-   Regression → Average.
-   Classification → Majority Vote.
-   Random Forest → Less Overfitting.

------------------------------------------------------------------------

# 📝 One-Line Revision

-   Random Forest → Multiple Decision Trees
-   Bootstrap Sampling → Sampling with Replacement
-   Bagging → Bootstrap + Multiple Trees
-   Voting → Majority Vote
-   RandomForestRegressor → Continuous Numerical Prediction
-   RandomForestClassifier → Categorical Prediction
-   Regression → Average
-   Classification → Majority Vote
