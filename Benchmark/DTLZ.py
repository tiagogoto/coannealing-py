import numpy as np
import math

class DTLZ1:
    def __init__(self, NumberOfVariable, NumberOfFunction):
        self.Nov = NumberOfVariable
        self.NoF = NumberOfFunction
        self.maxv = np.ones(NumberOfVariable)
        self.minv = np.zeros(NumberOfVariable)
    def evaluate(self, x):

        return [f1, f2, f3]import numpy as np
import math

class DTLZ1:
    def __init__(self, NumberOfVariable,NumberOfFunction):
        self.Nov = NumberOfVariable
        self.NoF = NumberOfFunction
        self.maxv = np.ones(NumberOfVariable)
        self.minv = np.zeros(NumberOfVariable)
    def evaluate(self, x):
        for k in range(0, self.nov):
            sum = sum + math.pow((x[k] - 0.5), 2) - math.cos(20 * math.pi * (x[k] - 0.5))
        g = 100 * (5 + sum);
        f1 = 0.5 * x[0] * x[1] * (1 + g)
        f2 = 0.5 * x[0] * (1 - x[1]) * (1 + g)
        f3 = 0.5 * (1 - x [0]) * (1 + g)
        return [f1, f2, f3]