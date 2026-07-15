# Machine Learning (ML) - Short Notes

## What is Machine Learning?
Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn from data and make predictions without being explicitly programmed.

---

# Types of Machine Learning

## 1. Supervised Learning
- Uses labeled data.
- Input (X) and Output (Y) are known.

### Types
- **Regression** → Predicts continuous numeric values.
- **Classification** → Predicts categories/classes.

## 2. Unsupervised Learning
- Uses unlabeled data.
- Finds hidden patterns or groups.

## 3. Reinforcement Learning
- Learns using rewards and penalties.

---

# Labeled Data

A dataset containing both input (Features) and output (Target).

Example:

| Age | BMI | Charges |
|-----|-----|---------|
| 25 | 27.5 | 5000 |

---

# Regression

Predicts continuous numeric values.

Examples:
- House Price Prediction
- Salary Prediction
- Insurance Cost Prediction

---

# Classification

Predicts categories/classes.

Examples:
- Spam Detection
- Disease Prediction
- Fake News Detection

---

# Linear Regression

Linear Regression is a **Supervised Machine Learning Regression algorithm** used to predict continuous numerical values by finding the relationship between input features (X) and target variable (Y).

### Examples
- House Price Prediction
- Salary Prediction
- Insurance Cost Prediction

---

# Types of Linear Regression

## 1. Simple Linear Regression
- One input feature.
- One output.

### Formula

```text
Y = mX + c
```

Where:
- Y = Dependent Variable
- X = Independent Variable
- m = Slope
- c = Intercept

---

## 2. Multiple Linear Regression
- Two or more input features.
- One output.

Our project uses **Multiple Linear Regression** because it has six input features.

---

# Independent Variable (X)

Input features used for prediction.

Example:
- Age
- Sex
- BMI
- Children
- Smoker
- Region

---

# Dependent Variable (Y)

Target variable to be predicted.

Example:
- Charges

---

# Machine Learning Workflow

```text
Import Libraries
        ↓
Import Dataset
        ↓
EDA
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Import Model
        ↓
Create Model
        ↓
Train Model
        ↓
Prediction
        ↓
Evaluation
        ↓
Save Model (.pkl)
        ↓
Deploy (Streamlit)
```

---

# Step 1 - Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

---

# Step 2 - Import Dataset

```python
df = pd.read_csv("insurance.csv")
```

CSV = Comma Separated Values

---

# Step 3 - Exploratory Data Analysis (EDA)

```python
df.head()
```
Shows first 5 rows.

```python
df.tail()
```
Shows last 5 rows.

```python
df.shape
```
Returns (Rows, Columns)

```python
df.info()
```
Shows data types, null values and memory usage.

```python
df.describe()
```
Shows statistical summary.

```python
df.isnull().sum()
```
Checks missing values.

```python
df.duplicated().sum()
```
Checks duplicate rows.

```python
df.drop_duplicates()
```
Removes duplicate rows.

---

# Step 4 - Data Preprocessing

## Label Encoding

Converts categorical(text) data into numerical values.

Example:

```text
Male   → 1
Female → 0

Yes    → 1
No     → 0
```

```python
le = LabelEncoder()

df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])
```

---

# Step 5 - Feature Selection

```python
X = df[['age','sex','bmi','children','smoker','region']]
```

Features (Input)

```python
y = df['charges']
```

Target (Output)

---

# Step 6 - Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

- `test_size = 0.2` → 20% Testing, 80% Training
- `random_state = 42` → Same random split every time

---

# Step 7 - Create Model

```python
lr = LinearRegression()
```

Creates an empty Linear Regression model.

---

# Step 8 - Train Model

```python
lr.fit(X_train, y_train)
```

Trains the model using training data.

---

# Step 9 - Prediction

```python
y_pred = lr.predict(X_test)
```

Predicts output for unseen data.

---

# Step 10 - Model Evaluation

## MAE (Mean Absolute Error)

```python
mean_absolute_error(y_test, y_pred)
```

Average absolute error. Lower is better.

---

## MSE (Mean Squared Error)

```python
mean_squared_error(y_test, y_pred)
```

Average squared error. Lower is better.

---

## RMSE (Root Mean Squared Error)

```python
rmse = np.sqrt(mse)
```

Square root of MSE. Lower is better.

---

## R² Score

```python
r2_score(y_test, y_pred)
```

Closer to **1** = Better model.

---

# Step 11 - Save Model

```python
pickle.dump(lr, open("model.pkl", "wb"))
```

- `wb` = Write Binary

---

# Step 12 - Load Model

```python
model = pickle.load(open("model.pkl", "rb"))
```

- `rb` = Read Binary

---

# Step 13 - Streamlit

## Install

```bash
pip install streamlit
```

## Run

```bash
streamlit run app.py
```

---

# Streamlit Components

```python
st.title()
```
Creates title.

```python
st.write()
```
Displays text.

```python
st.number_input()
```
Takes numeric input.

```python
st.selectbox()
```
Creates dropdown.

```python
st.button()
```
Creates button.

```python
st.success()
```
Displays success message.

---

# Medical Insurance Cost Prediction Project

## Dataset
- insurance.csv

## Features
- Age
- Sex
- BMI
- Children
- Smoker
- Region

## Target
- Charges

## Algorithm
- Multiple Linear Regression

## Libraries Used
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pickle
- Streamlit

---

# Project Workflow

```text
Dataset
    ↓
EDA
    ↓
Encoding
    ↓
Feature Selection
    ↓
Train-Test Split
    ↓
Linear Regression
    ↓
Train Model
    ↓
Prediction
    ↓
Evaluation
    ↓
Save Model (.pkl)
    ↓
Streamlit GUI
```

---

# Interview One-Liners

- Machine Learning → Learning from data.
- Supervised Learning → Uses labeled data.
- Regression → Predicts continuous values.
- Classification → Predicts categories.
- Linear Regression → Predicts continuous values using a linear relationship.
- Simple Linear Regression → One input feature.
- Multiple Linear Regression → Multiple input features.
- X → Features (Input).
- y → Target (Output).
- Label Encoding → Converts text into numbers.
- Train-Test Split → Splits data into training and testing sets.
- `fit()` → Trains the model.
- `predict()` → Predicts output.
- MAE, MSE, RMSE → Error metrics.
- R² Score → Performance metric (Closer to 1 is better).
- `pickle.dump()` → Save model.
- `pickle.load()` → Load model.
- Streamlit → Build Machine Learning GUI.