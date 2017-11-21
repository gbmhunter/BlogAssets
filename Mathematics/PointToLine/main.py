import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

pointX1 = np.array([1, 3, 3])
pointX2 = np.array([2, 5, 5])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point.dot(normal)

# create x,y
# xx, yy = np.meshgrid(range(10), range(10))

# calculate corresponding z
# z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
# plt3d = plt.figure().gca(projection='3d')

fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')

# ax.plot_surface(xx, yy, z, alpha=0.2)

# Plot X1 and X2
ax.scatter(pointX1[0] , pointX1[1] , pointX1[2],  color='green')
ax.scatter(pointX2[0] , pointX2[1] , pointX2[2],  color='green')

# Create line through X1, X2
lineX = []
lineY = []
lineZ = []

index = np.linspace(-0.5,1.5,11)
for i in np.nditer(index):
    lineX.append(pointX1[0] + (pointX2[0] - pointX1[0])*i)
    lineY.append(pointX1[1] + (pointX2[1] - pointX1[1])*i)
    lineZ.append(pointX1[2] + (pointX2[2] - pointX1[2])*i)

ax.plot(lineX, lineY, lineZ)

# Create third point, X
pointX = np.array([3, 4, 1])
ax.scatter(pointX[0] , pointX[1] , pointX[2],  color='blue')

plt.show()