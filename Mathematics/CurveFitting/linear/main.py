#!/usr/bin/env python3
"""
This script calulates the best fit linear curve (linear regression)
to a set of given (x, y) data points
"""

import matplotlib.pyplot as plt
plt.switch_backend('agg') # Allow matplotlib to work in Docker

import numpy as np

pointsX = np.array([2, 3, 6, 7])
pointsY = np.array([1, 7, 5, 9])

# Ax = B
# where:
# A11 = \sum x_i^2
# A12 = \sum x_i
# A21 = \sum x_i
# A22 = n (number of points)
# x = [a \\ b]
# B = [ \sum x_i y_i \\ \sum y_i ]
A11 = np.power(pointsX, 2).sum()
A12 = pointsX.sum()
A21 = A12
A22 = pointsX.size

B1 = (pointsX*pointsY).sum()
B2 = pointsY.sum()

print(f'A11 = {A11}, A12 = {A12}, A21 = {A21}, A22 = {A22}, B1 = {B1}, B2 = {B2}')

A = np.array([[A11, A12], [A21, A22]])
B = np.array([[B1], [B2]])

# Solve for x. Ax = B so x = A-1*B
x = np.dot(np.linalg.inv(A), B)

print(f'x = {x}')

fig, ax = plt.subplots()

# Plot points
points = ax.scatter(pointsX, pointsY, color='green', label='Data Points')

# Plot best fit
bestFitX = np.array([pointsX.min() - 1, pointsX.max() + 1])
bestFitY = x[0]*bestFitX + x[1] # x[0] is a and x[1] is b in the line y(x) = ax + b
best_fit, = ax.plot(bestFitX, bestFitY, color='blue', label='Line Of Best Fit')

# Draw in error lines
for index, point in enumerate(pointsX):
    pointOnLineX = pointsX[index]
    pointOnLineY = x[0]*pointOnLineX + x[1]

    #ax.arrow([pointsX[index], pointOnLineX], [pointsY[index], pointOnLineY], color='red', linestyle='dashed')
    ax.annotate(s='', xy=(pointsX[index], pointsY[index]), xytext=(pointOnLineX, pointOnLineY), arrowprops=dict(arrowstyle='<->', color='red', linestyle='dashed'), color='red')

ax.text(2, 2, 'error', color='red', rotation=90)

plt.title('Linear Curve Fitting\n(Least Squares Approach)')
plt.xlabel('x')
plt.ylabel('y')

ax.legend([points, best_fit], ['Data points', 'Line of best fit, y = ax + b'])

plt.savefig('graph.png')