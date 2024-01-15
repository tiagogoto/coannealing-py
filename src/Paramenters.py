import numpy as np


class Paramenters:
    def __init__(self, Problem, **kwargs):
        defaultkwargs = {'Cmax': 20, 'N':1000, 'Tmax':300, 'Tmin':0.000000001, 'rmax':5,'SL':100, 'HL':50, 'strategy':3, 'alpha':0.95 }
        kwargs = defaultkwargs | kwargs
        self.Cmax = kwargs["Cmax"]
        self.Tmax = kwargs["Tmax"]
        self.Tmin = kwargs["Tmin"]
        self.alpha = kwargs["alpha"]
        self.N = kwargs["N"]
        self.rmax = kwargs["rmax"]
        self.SL = kwargs["SL"]
        self.HL = kwargs["HL"]
        self.C = np.ones(Problem.Nov)
        self.strategy = kwargs["strategy"]
        self.accepted = 0
        self.rejected = 0

    def positive_feedback(self, Index):
        if self.strategy == 1:
            self.C[Index] = 1
        elif self.strategy == 2:
            self.C[Index] = round(self.C[Index] / 2)
        elif self.strategy == 3:
            self.C[Index] -= 1
            if self.C[Index] < 1:
                self.C[Index] = 1
        else:
            if self.phase:
                self.C[Index] = 1
            else:
                self.C[Index] -= 3
                if self.C[Index] < 1:
                    self.C[Index] = 1

    def negative_Feedback(self, Index):
        self.C[Index] += 1
    def increase_accepted(self):
        self.accepted += 1
    def increase_rejected(self):
        self.rejected +=1
    def reset_paramenters(self):
        self.accepted = 0
        self.rejected = 0
        
