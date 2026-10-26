# Task 11: a) Random Forest   b) Boosting (AdaBoost)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

# a) Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=1).fit(Xtr, ytr)
rp = rf.predict(Xte)
print("a) Random Forest")
print("   Accuracy:", round(accuracy_score(yte, rp), 3))
print("   Feature importances:", rf.feature_importances_.round(3))

# b) Boosting (AdaBoost)
ab = AdaBoostClassifier(n_estimators=50, random_state=1).fit(Xtr, ytr)
ap = ab.predict(Xte)
print("\nb) AdaBoost (Boosting)")
print("   Accuracy:", round(accuracy_score(yte, ap), 3))
print("   Confusion Matrix:\n", confusion_matrix(yte, ap))
