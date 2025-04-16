#!../../venv/bin/python
from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])


points_deg = [30, 45, 60, 90, 120, 150, 180, 270];
points = np.radians(points_deg);

x = np.cos(points);
y = np.sin(points);

plt.scatter(x, y, marker='X')


for i in range(len(points)):
    plt.annotate(
        f"{points_deg[i]} °, {points[i]:0.2f}",
        xy = (x[i], y[i]),
        xytext=(+10, +0), textcoords='offset points'
    )


plt.show()
