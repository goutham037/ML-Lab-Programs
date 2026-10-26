# Task 3: Dimensionality reduction using PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X, y = iris.data, iris.target
print("Original shape:", X.shape)

# Standardize the data
X_std = StandardScaler().fit_transform(X)

# Apply PCA: reduce 4 features -> 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)
print("Reduced shape :", X_pca.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_.round(3))
print("Total variance retained:", round(pca.explained_variance_ratio_.sum()*100, 2), "%")

# Plot the 2 principal components
plt.figure(figsize=(7, 5))
for i, name in enumerate(iris.target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=name)
plt.xlabel('PC 1'); plt.ylabel('PC 2'); plt.title('PCA on Iris Dataset')
plt.legend(); plt.show()
