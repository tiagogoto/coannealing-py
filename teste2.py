import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
import src.Benchmark as benchmark
#import src.Coannealing as Coannealing
import src.Archive.Archive as Archive
from src.Archive.GiftWrapping import GiftWrapping2D
import src.Paramenters as Paramenters
from src.Coannealing import Coannealing

Problem  = benchmark.get_problem(name="ZDT1", NumberofFunction=2, NumberofVariable = 30)
paramenters = Paramenters.Paramenters(Problem, N=300, Tmax = 10, Tmin=0.0000000001, SL= 100, HL=50) 
archive = Archive.Archive(Problem, paramenters)
coa = Coannealing(paramenters)
#Archive.init_archive(Problem)
#[xi, CurrentSolution, ind] = Archive.select_x()
#print(xi)
#[xj, ind] = coa.nextsol(xi, Problem, paramenters)
#print(xj)



coa.Run(Problem, archive, paramenters)


fig, axs = plt.subplots()
axs = plt.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1])
plt.show()