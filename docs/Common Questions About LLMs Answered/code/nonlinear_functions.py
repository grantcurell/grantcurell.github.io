import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Generate sample data resembling a sine wave
np.random.seed(0)
X = np.linspace(0, 10, 100)
y_true = np.sin(X) + np.random.randn(100) * 0.1  # Sine wave with added noise

# Linear Regression
lr = LinearRegression()
lr.fit(X.reshape(-1, 1), y_true)
y_lr = lr.predict(X.reshape(-1, 1))

# Non-linear Activation Function (Polynomial)
degree = 5  # Higher-degree polynomial transformation
X_poly = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(X.reshape(-1, 1))
lr_poly = LinearRegression()
lr_poly.fit(X_poly, y_true)
y_poly = lr_poly.predict(X_poly)

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y_true, label='True Data', color='b')
plt.plot(X, y_lr, label='Linear Regression', color='r', linestyle='--')
plt.plot(X, y_poly, label=f'Non-linear Activation (Degree {degree})', color='g')

plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Linear Regression vs. Non-linear Activation Function (Sine-like Data, Degree {degree})')
plt.legend()
plt.grid(True)
plt.show()
