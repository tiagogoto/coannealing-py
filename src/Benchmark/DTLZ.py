import numpy as np
import math

class DTLZ1:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':12, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov = kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        sum = 0
        for k in range(2, self.Nov):
            sum = sum + math.pow((x[k] - 0.5), 2) - math.cos(20 * math.pi * (x[k] - 0.5))
        g = 100 * (10 + sum);
        f1 = 0.5 * x[0] * x[1] * (1 + g)
        f2 = 0.5 * x[0] * (1 - x[1]) * (1 + g)
        f3 = 0.5 * (1 - x [0]) * (1 + g)
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True


class DTLZ2:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':12, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov = kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        sum = 0
        for k in range(2, self.Nov):
            sum = sum + math.pow((x[k] - 0.5), 2)
        g =  sum
        f1 = math.cos(x[0] * math.pi / 2) * math.cos(x[1] * math.pi / 2) * (1 + g)
        f2 = math.cos(x[0] * math.pi / 2) * math.sin(x[1] * math.pi / 2) * (1 + g)
        f3 = math.sin(x[0] * math.pi / 2) * (1 + g)
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True
    
class DTLZ3:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':12, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov = kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        sum = 0
        for k in range(2, self.Nov):
            sum = sum + math.pow((x[k] - 0.5), 2) - math.cos(20 * math.pi * (x[k] - 0.5))
        g = 100 * (10 + sum)
        f1 = math.cos(x[0] * math.pi / 2) * math.cos(x[1]* math.pi / 2) * (1 + g)
        f2 = math.cos(x[0] *math.pi / 2) * math.sin(x[1] *  math.pi / 2) *  (1 + g)
        f3 = math.sin(x[0] * math.pi / 2 ) * (1 + g)
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True

class DTLZ4:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':12, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov = kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        sum = 0
        for k in range(2, self.Nov):
            sum = sum + math.pow((x[k] - 0.5), 2)
        g =  sum
        f1 = math.cos(x[0]**100 * math.pi / 2) * math.cos(x[1]**100 * math.pi / 2) * (1 + g)
        f2 = math.cos(x[0]**100 * math.pi / 2) * math.sin(x[1]**100 *  math.pi / 2) *  (1 + g)
        f3 = math.sin(x[0]**100 * math.pi / 2 ) * (1 + g)
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True

class DTLZ5:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':12, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov = kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        sum = 0
        for k in range(2, self.Nov):
            sum = sum + math.pow((x[k] - 0.5), 2)
        g = (sum)
        theta1 = x[0] 
        theta2 = (math.pi * (1 + 2 * g * x[1])) / (4 * (1 + g))
        f1 = (1 + g) * math.cos(math.pi * theta1 * 0.5 ) * math.cos(theta2)
        f2 = (1 + g) * math.cos(math.pi * theta1 * 0.5 ) * math.sin(theta2)
        f3 = (1 + g) * math.sin(0.5 * theta1 * math.pi) 
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True
    
class DTLZ7:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':10, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov = kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov)
        self.minv = np.zeros(self.Nov)
    def evaluate(self, x):
        sum = 0
        for k in range(2, self.Nov):
            sum = sum + x[k]
        g = 1 + 9/20 * sum;
        f1 = x[0] 
        f2 = x[1]
        h = 0
        for jj in [f1, f2]:
            h = h + jj/(1 + g) * (1 + math.sin(3* math.pi * jj))
        h = 3-h
        f3 = (1 + g) * h
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True