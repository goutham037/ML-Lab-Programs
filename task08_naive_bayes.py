# Task 8: Naive Bayes Classification
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_wine()
X, y = data.data, data.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

model = GaussianNB().fit(Xtr, ytr)
pred = model.predict(Xte)

print("Naive Bayes Accuracy:", round(accuracy_score(yte, pred), 3))
print("\nConfusion Matrix:\n", confusion_matrix(yte, pred))
print("\nClassification Report:\n", classification_report(yte, pred, target_names=data.target_names))

# Predict a new sample
sample = Xte[0].reshape(1, -1)
print("Sample predicted class:", data.target_names[model.predict(sample)[0]])
