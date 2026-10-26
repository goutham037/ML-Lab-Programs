# Task 5: Simple and Multiple Linear Regression
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

X, y = load_diabetes(return_X_y=True)

# ---------- Simple Linear Regression (one feature) ----------
x1 = X[:, [2]]            # BMI feature
xtr, xte, ytr, yte = train_test_split(x1, y, test_size=0.2, random_state=1)
slr = LinearRegression().fit(xtr, ytr)
pred = slr.predict(xte)
print("Simple Linear Regression")
print("  Slope:", round(slr.coef_[0], 2), " Intercept:", round(slr.intercept_, 2))
print("  R2:", round(r2_score(yte, pred), 3),
      " RMSE:", round(mean_squared_error(yte, pred)**0.5, 2))

plt.scatter(xte, yte, label='Actual')
plt.plot(xte, pred, color='red', label='Predicted')
plt.title('Simple Linear Regression'); plt.legend(); plt.show()

# ---------- Multiple Linear Regression (all features) ----------
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)
mlr = LinearRegression().fit(Xtr, ytr)
pred = mlr.predict(Xte)
print("\nMultiple Linear Regression")
print("  R2:", round(r2_score(yte, pred), 3),
      " RMSE:", round(mean_squared_error(yte, pred)**0.5, 2))
