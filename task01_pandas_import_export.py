# Task 1: Import and export data using Pandas library functions
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name':  ['Ram', 'Sita', 'John', 'Asha', 'Ravi'],
    'Age':   [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 88, 72]
})
print("Original Data:\n", df)

# ---------- EXPORT ----------
df.to_csv('data/students.csv', index=False)
df.to_excel('data/students.xlsx', index=False)
df.to_json('data/students.json', orient='records')
print("\nData exported to CSV, Excel and JSON.")

# ---------- IMPORT ----------
data = pd.read_csv('data/students.csv')
print("\nImported from CSV:\n", data)

print("\nStatistical summary:\n", data.describe())
print("\nAverage Marks:", data['Marks'].mean())
print("Topper:", data.loc[data['Marks'].idxmax(), 'Name'])
