#python 3.8!
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit
import math
 
def lk():
    E=1      #elasticity module of material
    nu=(-0.3)  #poisson coeficient
    k=np.array([(1/2-nu/6), 1/8+nu/8, -1/4-nu/12, -1/8+3*nu/8, -1/4+nu/12,
     -1/8-nu/8, nu/6, 1/8-3*nu/8])
    KE = E/(1-nu**2)*np.array([[k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7]],
    [k[1], k[0], k[7], k[6], k[5], k[4], k[3], k[2]],
    [k[2], k[7], k[0], k[5], k[6], k[3], k[4], k[1]],
    [k[3], k[6], k[5], k[0], k[7], k[2], k[1], k[4]],
    [k[4], k[5], k[6], k[7], k[0], k[1], k[2], k[3]],
    [k[5], k[4], k[3], k[2], k[1], k[0], k[7], k[6]],
    [k[6], k[3], k[4], k[1], k[2], k[7], k[0], k[5]],
    [k[7], k[2], k[1], k[4], k[3], k[6], k[5], k[0]] ])
    return KE

def FEA(x, lk, penal):

    [nely, nelx]=np.shape(x)
    



    return J

def volfrac(x):
    

    return volf
