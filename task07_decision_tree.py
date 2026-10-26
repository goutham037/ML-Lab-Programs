# Task 7: Decision Tree classification and classify a new sample
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X, y = iris.data, iris.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=1)
clf.fit(Xtr, ytr)
pred = clf.predict(Xte)

print("Accuracy:", round(accuracy_score(yte, pred), 3))
print("\nClassification Report:\n", classification_report(yte, pred, target_names=iris.target_names))

# Classify a new sample
new = [[5.1, 3.5, 1.4, 0.2]]
print("New sample", new[0], "-> predicted:", iris.target_names[clf.predict(new)[0]])

# Visualize the tree
plt.figure(figsize=(10, 6))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title('Decision Tree'); plt.show()
