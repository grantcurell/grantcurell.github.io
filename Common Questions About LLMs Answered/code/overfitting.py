import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons

# Function to generate synthetic data
def generate_data(n_samples=300, noise=0.25, random_state=42):
    X, y = make_moons(n_samples=n_samples, noise=noise, random_state=random_state)
    return X, y

# Generate training data
X_train, y_train = generate_data(n_samples=300, noise=0.25, random_state=42)

# Generate new test data with increased noise
X_test_new, y_test_new = generate_data(n_samples=300, noise=0.5, random_state=24)  # Significantly increased noise

# Fit two models: one overfitted, one well-fitted
dt_overfit = DecisionTreeClassifier(random_state=42)
dt_overfit.fit(X_train, y_train)

dt_wellfit = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_wellfit.fit(X_train, y_train)

# Function to visualize the decision boundaries
def plot_decision_boundaries(X, y, model, title, subplot, xlim=(-1.5, 2.5), ylim=(-1, 1.5)):
    # Plotting decision regions
    x1 = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)
    x2 = np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 100)
    xx1, xx2 = np.meshgrid(x1, x2)
    Z = model.predict(np.c_[xx1.ravel(), xx2.ravel()])
    Z = Z.reshape(xx1.shape)

    subplot.contourf(xx1, xx2, Z, alpha=0.4)
    subplot.scatter(X[:, 0], X[:, 1], c=y, marker='o', s=100, edgecolor='k')
    subplot.set_xlim(xlim)
    subplot.set_ylim(ylim)
    subplot.set_title(title)

# Plotting
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

plot_decision_boundaries(X_train, y_train, dt_overfit, "Training Data - Overfitted Decision Tree", ax[0, 0])
plot_decision_boundaries(X_train, y_train, dt_wellfit, "Training Data - Well-fitted Decision Tree", ax[0, 1])
plot_decision_boundaries(X_test_new, y_test_new, dt_overfit, "New Data - Overfitted Decision Tree", ax[1, 0])
plot_decision_boundaries(X_test_new, y_test_new, dt_wellfit, "New Data - Well-fitted Decision Tree", ax[1, 1])

plt.tight_layout()
plt.show()
