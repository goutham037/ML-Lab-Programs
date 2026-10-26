# Task 6: Logistic Regression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()
X, y = data.data, data.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

# Scale features for better convergence
sc = StandardScaler()
Xtr, Xte = sc.fit_transform(Xtr), sc.transform(Xte)

model = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
pred = model.predict(Xte)

print("Accuracy:", round(accuracy_score(yte, pred), 3))
print("\nConfusion Matrix:\n", confusion_matrix(yte, pred))
print("\nClassification Report:\n", classification_report(yte, pred, target_names=data.target_names))
