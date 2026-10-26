# Task 9: KNN Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

# Scale features (KNN is distance based)
sc = StandardScaler()
Xtr, Xte = sc.fit_transform(Xtr), sc.transform(Xte)

model = KNeighborsClassifier(n_neighbors=5).fit(Xtr, ytr)
pred = model.predict(Xte)

print("KNN (k=5) Accuracy:", round(accuracy_score(yte, pred), 3))
print("\nConfusion Matrix:\n", confusion_matrix(yte, pred))
print("\nClassification Report:\n", classification_report(yte, pred, target_names=iris.target_names))
