# Multiobjective Optimization based on Simulated Annealing - CoAnnealing algorithm with Crystallization Factor

## Implementation on Python languagem




## Benchmark Function

Unconstrained Benchmark function with two objective function

* ZDT1
* ZDT2
* ZDT3
* ZDT6

Unconstrained Benchmark function with three objective function

* DTLZ1
* DTLZ2
* DTLZ5
* DTLZ7

Benchmark function with constraints:

* Binh and Korn
* Chenkong 


## Example to run benchmark function

``` python

import src.Benchmark as benchmark
import src.Paramenters as Paramenters
from src.Coannealing import Coannealing

Problem  = benchmark.get_problem(name="dtlz1")
paramenters = Paramenters.Paramenters(Problem, N=1000, Tmax = 1000, Tmin=0.001, SL= 200, HL=175,strategy=3, alpha=0.95)
coannealing = Coannealing(paramenters)

```


## Reference 

Goto, T. G. (2022). Propostas de heurísticas e estratégias de feedback aplicadas ao recozimento simulado (Doctoral dissertation, Universidade de São Paulo).


Martins, T. C., & Tsuzuki, M. S. G. (2015). EIT image regularization by a new Multi-Objective Simulated Annealing algorithm. Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS, 2015-Novem, 4069–4072. https://doi.org/10.1109/EMBC.2015.7319288


