import numpy as np
import math

class Binhkorn:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.array([5,3])
        self.minv = np.array([0,0])

    def evaluate(self, x):
        f1 = 4.0 * x[0] ** 2 + 4.0 * x[1] ** 2 
        f2 = (x[0] - 5.0) ** 2 + (x[1] - 5.0) ** 2
        return np.array([f1,f2])
    def restriction(self, x):
        g1 = (x[0] - 5.0) ** 2 + x[1] ** 2
        g2 = (x[0] - 8.0) ** 2 + (x[1] + 3.0) **2
        if g1 <= 25.0 and g2>= 7.7:
            res = True
        else:
            res = False
        return res
class ChanKong:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.array([20,20])
        self.minv = np.array([-20,-20])

    def evaluate(self, x):
        f1 = 2.0 + (x[0] - 2.0) ** 2 + (x[1] - 1.0 ) ** 2 
        f2 = 9 *x[0]- (x[1] - 1.0) ** 2
        return np.array([f1,f2])
    def restriction(self, x):
        g1 = (x[0]) ** 2 + x[1] ** 2
        g2 = x[0] - 3.0 * x[1] + 10.0 
        if g1 <= 225.0 and g2<= 0.0:
            res = True
        else:
            res = False
        return res
class ConstrEx:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.array([1,5])
        self.minv = np.array([0.1,0.0])

    def evaluate(self, x):
        f1 = x[0] 
        f2 = (1 + x[1]) / x[0]
        return np.array([f1,f2])
    def restriction(self, x):
        g1 = x[1] + 9.0 * x[0] 
        g2 = - x[1] + 9.0 * x[0] 
        if g1 >= 6.0 and g2 >= 1.0:
            res = True
        else:
            res = False
        return res
class TNK:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.array([math.pi,math.pi])
        self.minv = np.array([0.0,0.0])

    def evaluate(self, x):
        f1 = x[0] 
        f2 = x[1]
        return np.array([f1,f2])
    def restriction(self, x):
        g1 = - x[0] ** 2 - x[1] ** 2 + 1 + 0.1 * math.cos(16 * math.atan(x[0] / x[1])) 
        g2 = ( x[0] - 0.5) ** 2 + (x[1] - 0.5) ** 2 
        if g1 <= 0.0 and g2 <= 0.5:
            res = True
        else:
            res = False
        return res