# Task 12 b) BIRCH clustering algorithm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import Birch

X = load_iris().data

# BIRCH clustering
model = Birch(threshold=0.5, n_clusters=3)
labels = model.fit_predict(X)

print("Cluster labels:\n", labels)
print("Cluster sizes:", np.bincount(labels))

# Plot (first two features)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.xlabel('Sepal Length'); plt.ylabel('Sepal Width')
plt.title('BIRCH Clustering'); plt.show()
