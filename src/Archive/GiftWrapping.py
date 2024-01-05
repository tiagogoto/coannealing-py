# Implementation of Gift Wrapping (Jarvis March algorithm) for 2D and 3D,
# Author: Tiago G. Goto
#

import numpy as np
from scipy.spatial import ConvexHull


def crossproduct(point_a, point_b, point_c):
    orientation = (point_b[1] - point_a[1])*(point_c[0] - point_b[0]) \
        - (point_b[0] - point_a[0]) * (point_c[1] - point_b[1])
    if orientation > 0:
        orientation = 1
    elif orientation < 0:
        orientation = 2
    else:
        orientation = 0
    return orientation

def mensure_distance(point_a, point_b, point_c):
    distance_ab = np.sqrt(sum((point_a[:] - point_b[:]) ** 2))
    distance_ac = np.sqrt(sum((point_a[:] - point_c[:]) ** 2))
    # If distance of point_a to point_b is shorter than point_a to point_c, return 0 otherwise return 1 
    return np.argmin([distance_ab, distance_ac]) 


def GiftWrapping2D(points):
    l = 0
    [num_of_points, nof] = np.shape(points)
    convexhull = np.empty([0,nof])
    # check for most left point
    for i in range(1,num_of_points):
        if points[i][0] < points[l][0]:
            l = i
    point_p = l
    while True:
        convexhull = np.vstack([convexhull, points[point_p]])
        point_q = (point_p + 1) % num_of_points
        for x, value in enumerate(points):
            orientation = crossproduct(points[point_p], points[point_q], points[x])
            if orientation == 2:
                point_q = x
        point_p = point_q
        if (point_p == l):
            break
    return convexhull


    
def Squadarea(p, q, r):
    aux = q-p
    aux2 = r - p
    return np.cross(aux, aux2)
def SignedVolume(p,q,r,nextp):
    area = p *q
    return 1/6*np.dot()


def GiftWrapping3D(points):
    [lin, col] = np.shape(points)
    CH = ConvexHull(points)
    CH_points = np.empty([0, col])
    for convex in CH.simplices:
        CH_points = np.vstack([CH_points, convex])
    return CH_points
        


    


'''

archive = np.random.rand(20,2)

convexhull = GiftWrapping2D(archive)

from matplotlib import pyplot as plt

fig = plt.scatter(archive[:,0], archive[:,1], color='blue' )
fig = plt.scatter(convexhull[:,0], convexhull[:,1], color='red')
'''
