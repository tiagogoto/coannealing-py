import numpy as np
import matplotlib.pyplot as plt

class Paramenters:
    def __init__(self, Problem, **kwargs):
        defaultkwargs = {'Cmax': 20, 'N':1000, 'Tmax':300, 'Tmin':0.00000001, 'rmax':20,'SL':100, 'HL':50, 'strategy':3, 'alpha':0.85}
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
        self.add_sol = 0
        self.hist_accepted = np.empty(0, dtype=int)
        self.hist_rejected = np.empty(0, dtype=int)
        self.hist_temp = np.empty(0)
        self.hist_add = np.empty(0,dtype=int)
        self.hist_func_it = np.empty([0, Problem.Nof])
        self.hist_func_temp = np.empty([0, Problem.Nof])
        self.hist_crystallization = np.empty([0,Problem.Nov])
        self.specificHeat = np.empty([0, Problem.Nof])
        self.phase = 0
    
    def check_phase(self, temp):
        current_sh = np.mean(np.var(self.hist_func_it, axis=0))/temp ** 2
        aux = np.mean(self.specificHeat[-1,:]) / temp **2
        if current_sh < aux:
            self.phase = 1
        else:
            self.phase = 0


    def positive_feedback(self, Index):
        if self.strategy == 1:
            self.C[Index] = 1
        elif self.strategy == 2:
            self.C[Index] = int(self.C[Index] / 2)
            if self.C[Index] < 1:
                self.C[Index] = 1
        elif self.strategy == 3:
            self.C[Index] = self.C[Index] - 1
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
    def increase_add(self):
        self.add_sol += 1
    def register_func_ite(self,Fobj):
        self.hist_func_it = np.vstack((self.hist_func_it,Fobj))
        

    def reset_paramenters(self, Problem):
        self.accepted = 0
        self.rejected = 0
        self.add_sol = 0
        self.hist_func_it = np.empty([0, Problem.Nof])
    def reset_c(self):
        self.C.fill(1)

    def statistic_temp(self, temp):
        self.hist_temp = np.append(self.hist_temp, temp)
        self.hist_accepted = np.append(self.hist_accepted, self.accepted)
        self.hist_rejected = np.append(self.hist_rejected, self.rejected)
        self.hist_add = np.append(self.hist_add, self.add_sol)
        self.hist_crystallization = np.vstack((self.hist_crystallization, self.C))
        self.hist_func_temp = np.vstack((self.hist_func_temp, np.mean(self.hist_func_it, axis=0)))
        aux = np.std(self.hist_func_it, axis=0) #**2/ ( temp ** 2)
        self.specificHeat = np.vstack((self.specificHeat, aux))
    #def save_results(self, name):
    """    def calc_sh(self, fobj, temp):
        P1 = math.exp(-np.mean(fobj)/temp) / np.sum(math.exp(-np.mean(self.hist_func_it)/temp)
        C1 = np.sum()
    """

    def generate_plot(self):
        [fig, (axs, axs2,axs3, axs4)] = plt.subplots(4)
        axs.plot(self.hist_temp, self.hist_accepted, label="Accepted")
        axs.plot(self.hist_temp, self.hist_rejected, label="Rejected")
        axs.invert_xaxis() 
        axs.set_xscale('log')
        axs.set_xlabel("Temperature")
        axs.set_ylabel("Accepted and Rejected")
        axs.legend()
        nov = np.size(self.C)
        for i in range(0,nov):
            axs2.plot(self.hist_temp,self.hist_crystallization[:,i], label=f"C-{i}")
        axs2.invert_xaxis() 
        axs2.set_xscale('log')
        axs2.set_xlabel("Temperature")
        axs2.set_ylabel("Crystallization Factor")
        axs3.plot(self.hist_temp, self.specificHeat, label=" Standard deviation")
        axs3.invert_xaxis() 
        axs3.set_xscale('log')
        axs3.set_yscale('linear')
        axs3.set_xlabel("Temperature")
        axs3.set_ylabel("Standard deviation")
        axs3.legend()
        axs4.plot(self.hist_temp, self.hist_func_temp, label="Objective Function")
        axs4.invert_xaxis() 
        axs4.set_xscale('log')
        axs4.set_xlabel("Temperature")
        axs4.set_ylabel("Objective Function")
        axs4.legend()
        plt.show()
        
    def save_statistic(self):
        name = f"{Problem.name}-datas.txt"
        np.savetxt(name, (self.hist_temp, self.hist_accepted, self.hist_rejected), delimiter=",")



    
        
