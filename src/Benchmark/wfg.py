import numpy as np
import math

class Wfg1:
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