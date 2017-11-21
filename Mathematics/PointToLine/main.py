import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

pointP1 = np.array([1, 3, 3])
pointP2 = np.array([2, 5, 5])

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
ax.scatter(pointP1[0] , pointP1[1] , pointP1[2],  color='green')
ax.text(pointP1[0]+0.1, pointP1[1]+0.1, pointP1[2]+0.1, r'$P1' + '$', horizontalalignment='left', verticalalignment='top')

ax.scatter(pointP2[0] , pointP2[1] , pointP2[2],  color='green')
ax.text(pointP2[0]+0.1, pointP2[1]+0.1 , pointP2[2]+0.1, r'$P2' + '$', horizontalalignment='left', verticalalignment='top')

# Create line through X1, X2
lineX = []
lineY = []
lineZ = []

index = np.linspace(-0.5,1.5,11)
for i in np.nditer(index):
    lineX.append(pointP1[0] + (pointP2[0] - pointP1[0])*i)
    lineY.append(pointP1[1] + (pointP2[1] - pointP1[1])*i)
    lineZ.append(pointP1[2] + (pointP2[2] - pointP1[2])*i)

ax.plot(lineX, lineY, lineZ)

# Create third point, P3 (not on line)
pointP3 = np.array([3, 4, 2])
ax.scatter(pointP3[0] , pointP3[1] , pointP3[2],  color='blue')
ax.text(pointP3[0]+0.1, pointP3[1]+0.1, pointP3[2]+0.1, r'$P3' + '$', horizontalalignment='left', verticalalignment='top')

# Show distance between line and point

lineX = []
lineY = []
lineZ = []

utop = ((pointP3[0] - pointP1[0])*(pointP2[0] - pointP1[0]) + (pointP3[1] - pointP1[1])*(pointP2[1] - pointP1[1]) + (pointP3[2] - pointP1[2])*(pointP2[2] - pointP1[2]))
ubottom = ((pointP2[0] - pointP1[0])^2 + (pointP2[1] - pointP1[1])^2 + (pointP2[2] - pointP1[2])^2)

u = utop / ubottom
    
print((pointP3[0] - pointP1[0])*(pointP2[0] - pointP1[0]))    
print('pointP1 = ' + str(pointP1))    
print('pointP2 = ' + str(pointP2))    
print('pointP3 = ' + str(pointP3))    
print('utop = ' + str(utop))
print('ubottom = ' + str(ubottom))
print('u = ' + str(u))

# Plot point P4, point on line closest to P3
pointP4 = np.array([pointP1[0] + (pointP2[0] - pointP1[0])*u, pointP1[1] + (pointP2[1] - pointP1[1])*u, pointP1[2] + (pointP2[2] - pointP1[2])*u])
ax.scatter(pointP4[0] , pointP4[1] , pointP4[2],  color='blue')

# Draw line between P3 and line (shortest distance)
vectorP3P4 = np.array([(pointP4[0] - pointP3[0]), (pointP4[1] - pointP3[1]), (pointP4[2] - pointP3[2])])
index = np.linspace(0,1,11)
lineX = []
lineY = []
lineZ = []
for i in np.nditer(index):
    lineX.append(pointP3[0] + vectorP3P4[0]*i)
    lineY.append(pointP3[1] + vectorP3P4[1]*i)
    lineZ.append(pointP3[2] + vectorP3P4[2]*i)
ax.plot(lineX, lineY, lineZ, linestyle='--')

percentageFromP3ToP4 = 0.8
ax.text(
    pointP3[0] + vectorP3P4[0]*percentageFromP3ToP4 + 0.1, 
    pointP3[1] + vectorP3P4[1]*percentageFromP3ToP4 + 0.1,
    pointP3[2] + vectorP3P4[2]*percentageFromP3ToP4 + 0.1,
    'distance', (vectorP3P4[0], vectorP3P4[1], vectorP3P4[2]), horizontalalignment='left', verticalalignment='top')

# ax.quiver(pointP3[0], pointP3[1], pointP3[2], vectorP3P4[0], vectorP3P4[1], vectorP3P4[2])

plt.show()