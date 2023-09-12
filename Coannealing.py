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

    def maxdom(self,  NewSolution, Archive, R):
        aux = np.empty(0,2)



        return xj

    def Run(self, Problem, Archive, Paramenters):
        Temp = Paramenters.Tmax
        Archive.
        xi =
        CurrentSolution = Problem.evaluate(xi)
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










