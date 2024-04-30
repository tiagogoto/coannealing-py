# Multiobjective Optimization based on Simulated Annealing - CoAnnealing algorithm with Crystallization Factor

## Implementation on Python




## Benchmark Function

Unconstrained Benchmark function with two objective function

* ZDT1
* ZDT2
* ZDT3
* ZDT6
* Kursawe function (name = 'kursawe')

Unconstrained Benchmark function with three objective function

* DTLZ1
* DTLZ2
* DTLZ5
* DTLZ7
* Viennet function (name = 'viennet')

Benchmark function with constraints:

* Binh and Korn function, (name='binhkorn')
* Chankong and Haimes function, (name='chankong')
* Constr-Ex problem (name= 'constrex')




## An example to execute a benchmark function

``` python

import src.Benchmark as benchmark
import src.Paramenters as Paramenters
from src.Coannealing import Coannealing

Problem  = benchmark.get_problem(name="zdt1")
paramenters = Paramenters.Paramenters(Problem, N=500, Tmax = 200, Tmin=0.00000001, SL= 100, HL=75 strategy=3, alpha=0.95)
coannealing = Coannealing(paramenters)

```
## Class for a Custom Objective Function
For the application of CoAnneling in an optimization problem, the construction of a class for the objective function is essential. The class needs to be in the above format. 

Where Nov variable is a number of variables, Nof is the number of objective functions, maxv is a numpy array containing the max values for each variable. The minv is a numpy array containing the minimum values for each variable. 

The class needs to have two methods, the function evaluate that evaluate the objective functions and return numpy arrays with all objectives value. The second method, function restriction, evaluates the constraints of the objective function. The parameters must be numpy arrays with values of variables. The function returns a Boolean. If the solution satisfies the constraint, return true, and if it is not satisfied, return false.

```
class problem:
    def __init__(self, **kwargs):
        self.Nov = # number of variables
        self.Nof = # number of objective functions
        self.maxv = # a numpy.array([]) with max value for each variable 
        self.minv = # a numpy.array([]) with minimum 
    
    def evaluate(x):
        return numpy.array([f1, f2, f3])

    def restriction(x):
        return boolean
```



## References 

Goto, T. G. (2022). Propostas de heurísticas e estratégias de feedback aplicadas ao recozimento simulado (Doctoral dissertation, Universidade de São Paulo).


Martins, T. C., & Tsuzuki, M. S. G. (2015). EIT image regularization by a new Multi-Objective Simulated Annealing algorithm. Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS, 2015-Novem, 4069–4072. https://doi.org/10.1109/EMBC.2015.7319288


