import numpy as np
import math

class Fonsecaf:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov) * 4.0
        self.minv = np.ones(self.Nov) * (-4.0)

    def evaluate(self, x):
        f1 = 1.0 - math.exp(-np.sum((x[0:self.Nov-1]) - 1 / math.sqrt(self.Nov)) ** 2)
        f2 = 1.0 - math.exp(-np.sum((x[0:self.Nov-1]) + 1 / math.sqrt(self.Nov)) ** 2)
        return np.array([f1,f2])
    def restriction(self, x):
        return True

class Kursawe:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':3, 'NumberofFunction':2}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov) * 5.0
        self.minv = np.ones(self.Nov) * (-5.0)

    def evaluate(self, x):
        aux = np.sum(-10.0 * math.exp(-0.20 *math.sqrt(x[i]**2 + x[i+1]**2)) for i in range(0,self.Nov-1))
        f1 = aux#np.sum(-10.0 * math.exp(-0.2 * math.sqrt(x[0:2] ** 2 + x[0:2] ** 2)))
        f2 = np.sum(abs(i) ** 0.8 + 5 * math.sin(i ** 3) for i in x)
        return np.array([f1,f2])
    def restriction(self, x):
        return True
class Viennet:
    def __init__(self, **kwargs):
        defaultkwargs = { 'NumberofVariable':2, 'NumberofFunction':3}
        kwargs = defaultkwargs | kwargs
        self.Nov =  kwargs['NumberofVariable']
        self.Nof = kwargs['NumberofFunction']
        self.maxv = np.ones(self.Nov) * 3.0
        self.minv = np.ones(self.Nov) * (-3.0)

    def evaluate(self, x):
        f1 = 0.5 * (x[0] ** 2 + x[1] **2 ) + math.sin(x[0] ** 2 + x[1] **2)
        f2 = ((3* x[0] - 2 * x[1] +4) ** 2) / 8 + ((x[0] - x[1] + 1) ** 2 ) / 27 + 15
        f3 = 1 / (x[0] ** 2 + x[1] ** 2 + 1) - 1.1 * math.exp(- (x[0]**2 + x[1] ** 2))
        return np.array([f1, f2, f3])
    def restriction(self, x):
        return True