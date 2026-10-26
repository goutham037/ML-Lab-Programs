# Task 4: Data Visualization techniques
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

df = load_iris(as_frame=True).frame
df['species'] = load_iris().target_names[load_iris().target]

# 1. Line plot
df['sepal length (cm)'].plot(kind='line', title='Line Plot')
plt.show()

# 2. Histogram
df['sepal width (cm)'].plot(kind='hist', bins=15, title='Histogram')
plt.show()

# 3. Bar plot (mean petal length per species)
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', title='Bar Plot')
plt.show()

# 4. Scatter plot
sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', hue='species')
plt.title('Scatter Plot'); plt.show()

# 5. Box plot
sns.boxplot(data=df, x='species', y='sepal length (cm)')
plt.title('Box Plot'); plt.show()

# 6. Correlation heatmap
sns.heatmap(df.iloc[:, :4].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap'); plt.show()
