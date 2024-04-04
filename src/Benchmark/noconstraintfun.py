import numpy as np
import math

class Fonsecaf:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.array([5,3])
        self.minv = np.array([0,0])

    def evaluate(self, x):
        f1 = 4 * x[0] ** 2 + 4 * x[1] ** 2 
        g =  1 + 9/29 * np.sum(x[1:30])
        h = 1 - math.sqrt(f1/g)
        f2 = g * h
        return np.array([f1,f2])
    def restriction(self, x):
        return True