#!../../venv/bin/python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 512, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X, C, 'r--', label='cos(x)')
plt.plot(X, S, 'g:', label='sin(x)')

plt.legend()

plt.show()
