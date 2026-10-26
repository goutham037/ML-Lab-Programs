# Task 12 a) K-Means clustering (with library and from scratch)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

X = load_iris().data

# ---------- WITH library ----------
km = KMeans(n_clusters=3, random_state=1, n_init=10).fit(X)
print("Library K-Means cluster sizes:", np.bincount(km.labels_))

# ---------- WITHOUT library (from scratch) ----------
np.random.seed(1)
k = 3
centroids = X[np.random.choice(len(X), k, replace=False)]
for _ in range(10):
    # assign each point to nearest centroid
    labels = np.array([np.argmin([np.linalg.norm(x - c) for c in centroids]) for x in X])
    # update centroids
    centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
print("Scratch K-Means cluster sizes:", np.bincount(labels))

# Plot the scratch result (first two features)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)
plt.title('K-Means Clustering'); plt.show()
