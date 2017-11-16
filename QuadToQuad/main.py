import numpy as np
from numpy.linalg import inv

print("Hello")

# Defined anti-clockwise
quad1 = np.array([
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0]])

quad2 = np.array([
    [10, 10],
    [10, 12],
    [12, 12],
    [12, 10]])

inputPoint = np.array([[0], [0]])


A = np.empty((0,8))
B = np.empty((0,1))

print(A)
print(B)

for i in range(len(quad1)):

    P = quad1[i]
    Q = quad2[i]

    #                 p1*A + p2*B + 1*C + 0*D +  0*E +  0*F + -p1q1*G,    -p2q1*H
    A = np.vstack([A, [P[0], P[1],  1,    0,     0,     0,    -P[0]*Q[0], -P[1]*Q[0]]])

    #                  q1
    B = np.vstack([B, [Q[0]]])



    #                 0*A +  0*B +  0*C + p1*D + p2*E + 1*F + -p1q2G +    -p2q2H  
    A = np.vstack([A, [0,    0,     0,    P[0],  P[1],  1,    -P[0]*Q[1], -P[1]*Q[1]]])

    #                  q2
    B = np.vstack([B, [Q[1]]])

print("A = " + str(A))

print("B = " + str(B))

Ainv = inv(A)
print("Ainv = " + str(Ainv))

# To find x, calculate Ainv*B
x = np.dot(Ainv, B)

print("x = " + str(x))

x = np.vstack([x, [1]])

# Find the transformation matrix T
T = x.reshape(3, 3)

print ("T = " + str(T))

# inputPoint3D
inputPoint3D = np.vstack([inputPoint, [1]])

outputPoint3D = np.dot(T, inputPoint3D)

print("outputPoint = " + str(outputPoint3D))
