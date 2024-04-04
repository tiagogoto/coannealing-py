import numpy as np
import matplotlib.pyplot as plt
import src.Archive.Archive as Archive
from src.Archive.GiftWrapping import GiftWrapping2D
import src.Paramenters as Paramenters
from src.Coannealing import Coannealing
import src.Benchmark as benchmark


Problem  = benchmark.get_problem(name="zdt3", NumberofFunction=2, NumberofVariable = 30)
paramenters = Paramenters.Paramenters(Problem, N=100, Tmax = 200, Tmin=0.000000000000001, SL= 50, HL=30, alpha=0.95) 
archive = Archive.Archive(Problem, paramenters)
archive.init_archive(Problem)


x = np.array([[0.03306742,3.78745377], [0.10518507,4.24311709], [0.47785883,3.99557194],[0.97519199,3.44381982], [0.99076962,3.36544784], [0.99558161,1.9879304 ], [0.86778763,1.37978348], [0.21528961,2.2555101 ], [0.03439174,3.46889163]])
print(archive.domination(x[0], x[1]))
[lin, col] = np.shape(x)
for i in range(1,2):
    for j in range(0,lin):
        if i != j:
            if archive.domination(x[i], x[j]):
                print(f'o item {i} domina {j}')


pf = archive.points_on_hull(x)
print(pf)