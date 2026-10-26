# Task 2: Data preprocessing techniques
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    'Age':    [25, 30, np.nan, 35, 40, 28],
    'Salary': [50000, np.nan, 61000, 58000, 52000, 49000],
    'Country': ['India', 'US', 'India', 'UK', 'US', 'UK'],
    'Buys':    ['No', 'Yes', 'No', 'Yes', 'Yes', 'No']
})
print("Original Data:\n", df)
print("\nMissing values:\n", df.isnull().sum())

# 1. Handle missing values (mean imputation)
imp = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imp.fit_transform(df[['Age', 'Salary']])

# 2. Encode categorical columns
df['Country'] = LabelEncoder().fit_transform(df['Country'])
df['Buys'] = LabelEncoder().fit_transform(df['Buys'])

# 3. Feature scaling
df[['Age', 'Salary']] = StandardScaler().fit_transform(df[['Age', 'Salary']])
print("\nAfter Preprocessing:\n", df.round(2))

# 4. Train-test split
X, y = df.drop('Buys', axis=1), df['Buys']
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.33, random_state=1)
print("\nTraining samples:", len(Xtr), " Testing samples:", len(Xte))
