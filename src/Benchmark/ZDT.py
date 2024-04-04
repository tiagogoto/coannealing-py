import math
import numpy as np

class ZDT1:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':30, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)

    def evaluate(self, x):
        f1 = x[0]
        g =  1 + 9/29 * np.sum(x[1:30])
        h = 1 - math.sqrt(f1/g)
        f2 = g * h
        return np.array([f1,f2])
    def restriction(self, x):
        return True

class ZDT2:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':30, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        f1 = x[0]
        g = 1 + 9/29 * np.sum(x[1:30])
        h = 1 - (f1/g) ** 2
        f2 = g * h
        return np.array([f1,f2])
    def restriction(self, x):
        return True
class ZDT3:
    def __init__(self,  **kwargs):
        defaultkwargs = { 'NumberofVariable':30, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        f1 = x[0]
        g = 1 + 9/29 * np.sum(x[1:30])
        h = 1 - np.sqrt(f1/g) - (f1/g) * math.sin(10 * math.pi * f1)
        f2 = g * h
        return np.array([f1,f2])
    def restriction(self, x):
        return True

class ZDT6:
    def __init__(self,  **kwargs):
        defaultkwargs = { 'NumberofVariable':10, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        f1 = 1 - math.exp(-4 * x[0]) * math.sin( 6 * math.pi * x[0]) ** 6
        g = 1 + 9/29 * ( np.sum(x[1:10]) / 9) ** (0.25)
        h = 1 -  (f1/g) ** 2
        f2 = g * h
        return np.array([f1,f2])
    def restriction(self, x):
        return True