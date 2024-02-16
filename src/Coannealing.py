import numpy as np
from scipy.special import expit
from Archive.Archive import Archive
from Paramenters import Paramenters



class Coannealing:
    def __init__(self, Paramenters):
        self.N = Paramenters.N

    def nextsol(self, x, Problem, Paramenters):
        xj = x.copy()
        rng = np.random.default_rng()
        ind = rng.integers(0,Problem.Nov, dtype= int)
        delr = (Problem.maxv[ind] - Problem.minv[ind])/4
        ek = 1
        val = 0
        status = 0
        while not status:
            val = 0
            if Paramenters.C[ind] < Paramenters.Cmax:
                SumRand = np.sum( np.random.uniform(-1,1,Paramenters.C[ind]))
                val = SumRand/Paramenters.C[ind] * delr * ek
            else:
                val = np.random.normal(0, expit(Paramenters.Cmax - Paramenters.C[ind] - 2)) * delr * ek
            res = Problem.restriction()
            aux = xj[ind] = xj[ind] + val
            if Problem.minv[ind] < aux and aux < Problem.maxv[ind] and res:
                status = 1
            else:
                status =0
        xj[ind] = xj[ind] + val
        return xj

    def maxdom(self, Solution, Archive, R):
        aux = np.ones(Archive.size())
        for i, count in zip(Archive.FobjValues, range(0,Archive.size())):
            for j in range(Archive.Nof):
                if Solution[j] < i[j]:
                    aux[count] = 0
                    break
                elif Solution[j] - i[j] < 1*10**(-6):
                    aux[count] = aux[count]
                else:
                    aux[count] = aux[count] * (Solution[j] - i[j]) * R[j]
        return aux.max()

    def Run(self, Problem, Archive, Paramenters):
        Temp = Paramenters.Tmax
        Archive.init_archive(Problem)
        [xi, CurrentSolution] = Archive.select_x()
        #CurrentSolution = Problem.evaluate(xi)
        while Temp > Paramenters.Tmin:
            count = 0
            Paramenters.Reset()
            while count < Paramenters.N and count < Paramenters.N/2:
                [xj, ind] =  nextsol(xi, Paramenters)
                NewSolution = Problem.evaluate(xj)
                R = Archive.maxmin()
                deltaE = self.MaxDom(NewSolution, Archive) - self.MaxDom(CurrentSolution, Archive)
                p = expit(-deltaE/Temp)
                RandNumber = np.random.rand()
                if deltaE <= 0 or RandNumber < p:
                    xi = xj.copy()
                    CurrentSolution = NewSolution.copy()
                    Paramenters.PositiveFeedback()
                    MaxDomination =
                    if MaxDomination <= 0:


                        if Archive.size() > Paramenters.SL:

                else:










