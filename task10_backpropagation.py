# Task 10: Back Propagation (Neural Network trained using backpropagation)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

# Scale inputs
sc = StandardScaler()
Xtr, Xte = sc.fit_transform(Xtr), sc.transform(Xte)

# MLPClassifier uses the back-propagation algorithm to train
model = MLPClassifier(hidden_layer_sizes=(8, 8), activation='relu',
                      max_iter=1000, random_state=1)
model.fit(Xtr, ytr)
pred = model.predict(Xte)

print("Back Propagation Neural Network")
print("Accuracy:", round(accuracy_score(yte, pred), 3))
print("Confusion Matrix:\n", confusion_matrix(yte, pred))
