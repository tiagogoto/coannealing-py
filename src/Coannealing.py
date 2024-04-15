import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from scipy.special import expit
from src.Archive.Archive import Archive
from src.Paramenters import Paramenters



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
                SumRand = np.sum( np.random.uniform(-1.0,1.0,int(Paramenters.C[ind])))
                #print(SumRand)
                val = SumRand/Paramenters.C[ind] * delr * ek
            else:
                val = np.random.normal(0, expit(Paramenters.Cmax - Paramenters.C[ind] - 2.0)) * delr * ek
            aux = xj[ind] + val
            aux2 = xj.copy()
            aux2[ind] += val
            res = Problem.restriction(aux2)
            if Problem.minv[ind] < aux and aux < Problem.maxv[ind] and res:
                status = 1
            else:
                status =0
        xj[ind] = xj[ind] + val
        return xj, ind

    def maxdom(self, Solution, Archive, R): # mudar esse esquema
        aux = np.ones(Archive.size())
        for i, count in zip(Archive.FobjValues, range(0,Archive.size())):
            for j in range(Archive.Nof):
                if Solution[j] < i[j]:
                    aux[count] = 0
                elif (Solution[j] - i[j]) < 1*10**(-6):
                    aux[count] = aux[count]
                else:
                    aux[count] = aux[count] * (Solution[j] - i[j]) * R[j]
        return aux.max()
    
        

    def Run(self, Problem, Archive, Paramenters):
        Temp = Paramenters.Tmax
        Archive.init_archive(Problem)
        [xi, CurrentSolution, ind] = Archive.select_x()
        r_count = 0
        aux_r =0
        lista_arquivo = np.empty([0,(Problem.Nof)])
        lista_tem_cont = np.empty([0,2])
        lista_accpeted =  np.empty([0,Problem.Nof])
        # matplotlib
        #CurrentSolution = Problem.evaluate(xi)
        while Temp > Paramenters.Tmin:
            count = 0
            Paramenters.reset_paramenters(Problem)
            while count < Paramenters.N and Paramenters.accepted < Paramenters.N/2:
                [xj, ind] =  self.nextsol(xi, Problem, Paramenters)
                NewSolution = Problem.evaluate(xj)
                R = Archive.maxmin()
                deltaE = self.maxdom(NewSolution, Archive, R) - self.maxdom(CurrentSolution, Archive, R)
                p = expit(-deltaE/Temp)
                RandNumber = np.random.rand()
                if deltaE <= 0 or RandNumber < p:
                    xi = xj.copy()
                    CurrentSolution = NewSolution.copy()
                    #debug
                    lista_accpeted = np.vstack((lista_accpeted, NewSolution))
                    #print("New solutions is accepted")
                    Paramenters.positive_feedback(ind)
                    MaxDomination = self.maxdom(CurrentSolution, Archive, R)
                    if MaxDomination <= 0:
                        #debug
                        
                        lista_arquivo = np.vstack((lista_arquivo,NewSolution))
                        
                        Archive.insert(xi, CurrentSolution)
                        #print("new solutions was add to Archive")                       
                        if Archive.size() > Paramenters.SL:
                            Archive.clusterization()
                            [is_belongs, index] = Archive.check_if_belongs(xi)
                            if not is_belongs:
                                r_count += 1
                                if r_count < Paramenters.rmax:
                                    Archive.insert(xi, CurrentSolution)
                                else:
                                    [xi, CurrentSolution, ind] = Archive.select_x()
                                    aux_r += 1
                                    r_count = 0
                            else:
                                r_count = 0
                    Paramenters.increase_accepted()        
                else:
                    Paramenters.negative_Feedback(ind)
                    Paramenters.increase_rejected()
                    #print("solução rejeitada!")
                Paramenters.register_func_ite(CurrentSolution)
                count += 1

                
                #print(f"Count: {count}, Archive size: {Archive.size()}, Accepted: {Paramenters.accepted}")
            Paramenters.statistic_temp(Temp)
            Paramenters.register_func_ite(CurrentSolution)
            Paramenters.check_phase(Temp)
            print(f"Temp: {Temp}, Archive size: {Archive.size()}")
            #Archive.save_archive(name="zdt1")
            Temp *= Paramenters.alpha
        #plt.ioff()
        np.savetxt('debug.txt', lista_arquivo, delimiter=',')
        np.savetxt('debug_accepted.txt', lista_accpeted, delimiter=",")
        Paramenters.generate_plot()    

                










