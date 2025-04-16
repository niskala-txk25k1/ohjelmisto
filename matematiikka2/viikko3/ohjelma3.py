#!../../venv/bin/python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 512, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(19.2, 4.8))

plt.plot(X, C, 'r--', label='cos(x)')
plt.plot(X, S, 'g:', label='sin(x)')

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.legend()

plt.show()
