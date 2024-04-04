import numpy as np
import matplotlib.pyplot as plt

class Paramenters:
    def __init__(self, Problem, **kwargs):
        defaultkwargs = {'Cmax': 20, 'N':1000, 'Tmax':300, 'Tmin':0.00000001, 'rmax':5,'SL':100, 'HL':50, 'strategy':3, 'alpha':0.85, 'rmax':10 }
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
        self.rmax = kwargs["rmax"]
        self.hist_accepted = np.empty(0, dtype=int)
        self.hist_rejected = np.empty(0, dtype=int)
        self.hist_temp = np.empty(0)
        self.hist_add = np.empty(0,dtype=int)
        self.hist_func_it = np.empty([0, Problem.Nof])
        self.hist_func_temp = np.empty([0, Problem.Nof])
        self.hist_crystallization = np.empty([0,Problem.Nov])

    def check_phase(self, ):
        

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

    def reset_paramenters(self):
        self.accepted = 0
        self.rejected = 0
        self.add_sol = 0
    def reset_c(self):
        self.C.fill(1)
    def statistic_temp(self, temp):
        self.hist_temp = np.append(self.hist_temp, temp)
        self.hist_accepted = np.append(self.hist_accepted, self.accepted)
        self.hist_rejected = np.append(self.hist_rejected, self.rejected)
        self.hist_add = np.append(self.hist_add, self.add_sol)
        self.hist_crystallization = np.vstack((self.hist_crystallization, self.C))
    #def save_results(self, name):
    def generate_plot(self):
        [fig, (axs, axs2)] = plt.subplots(2)
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
        plt.show()
    def save_statistic(self):
        name = f"{Problem.name}-datas.txt"
        np.savetxt(name, (self.hist_temp, self.hist_accepted, self.hist_rejected), delimiter=",")



    
        
