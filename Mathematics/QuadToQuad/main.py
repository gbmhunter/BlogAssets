import numpy as np
from numpy.linalg import inv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from PIL import Image

def GetQuad2QuadTransformationMatrix(quad1, quad2):    

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

    return T


def ShowTransformationPlot():
    # Defined anti-clockwise
    quad1 = np.array([
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0]])

    quad2 = np.array([
        [1, 2],
        [1, 4],
        [3, 4],
        [3, 2]])

    T = GetQuad2QuadTransformationMatrix(quad1, quad2)

    inputPoint = np.array([[0], [0]])

    # inputPoint3D
    inputPoint3D = np.vstack([inputPoint, [1]])

    outputPoint3D = np.dot(T, inputPoint3D)

    print("outputPoint = " + str(outputPoint3D))

    fig1 = plt.figure()
    ax = fig1.add_subplot(111, aspect='equal')
    patchA = []

    ax.add_patch(patches.Polygon(quad1, linewidth=1, edgecolor='b', facecolor='none'))

    textHAlign = ['right', 'right', 'left', 'left']
    textVAlign = ['top', 'bottom', 'bottom', 'top']

    for index, elem in enumerate(quad1):
        ax.text(elem[0], elem[1], r'$p_' + str(index+1) + '$', horizontalalignment=textHAlign[index], verticalalignment=textVAlign[index])

    ax.add_patch(patches.Polygon(quad2, linewidth=1, edgecolor='r', facecolor='none'))

    for index, elem in enumerate(quad2):
        ax.text(elem[0], elem[1], r'$q_' + str(index+1) + '$', horizontalalignment=textHAlign[index], verticalalignment=textVAlign[index])        

    # Draw arrows from each point p to it's paired point q
    for index, elem in enumerate(quad1):
        ax.arrow(elem[0], elem[1], quad2[index][0] - elem[0], quad2[index][1] - elem[1], facecolor='none', linewidth=1, edgecolor='#d8d8d8')


    plt.xlim([-1, 5])
    plt.ylim([-1, 5])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Quad-to-Quad Transformation')
    fig1.savefig('output.png', dpi=90, bbox_inches='tight')
    # plt.show()


# TRANSFORM IMAGE

def TransformImage():
    img = Image.open('hello-txt-outline-blue.png')

    oldWidth, oldHeight = img.size
    print('oldWidth = ' + str(oldWidth))
    print('oldHeight = ' + str(oldHeight))

    tImageOffestX = 450

    # Get a transformation matrix
    quad1 = np.array([
        [0, 0],
        [0, oldHeight],
        [oldWidth, oldHeight],
        [oldWidth, 0]])

    quad2 = np.array([
        [tImageOffestX, 0 + 50],
        [tImageOffestX + 50, oldHeight/2 + 50],
        [tImageOffestX + oldWidth - 100, oldHeight],
        [tImageOffestX + oldWidth, 0]])

    T = GetQuad2QuadTransformationMatrix(quad2, quad1)
    x = T.flatten()[:-1]
    print('x = ' + str(x))

    imgTransformed = img.transform((tImageOffestX + oldWidth, oldHeight), Image.PERSPECTIVE, x, Image.BICUBIC)
        
    # Show images
      
    # imgplt = plt.imshow(imgTransformed)

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')    
    ax.add_patch(patches.Polygon(quad1, linewidth=1, edgecolor='b', facecolor='none'))
    ax.add_patch(patches.Polygon(quad2, linewidth=1, edgecolor='r', facecolor='none'))
    ax.imshow(img)  
    ax.imshow(imgTransformed)  

    plt.xlim([-50, 950])
    plt.ylim([250, -50])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2D Quad-to-Quad Transformation With Image')
    plt.show()

# IMAGE ON GRAPH

ShowTransformationPlot()
TransformImage()




