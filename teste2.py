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

Problem  = benchmark.get_problem(name="zdt6")
paramenters = Paramenters.Paramenters(Problem, N=100, Tmax =10, Tmin=0.00000000001, SL= 100, HL=75,strategy=2, alpha=0.95) 
archive = Archive.Archive(Problem, paramenters)
coa = Coannealing(paramenters)
#Archive.init_archive(Problem)
#[xi, CurrentSolution, ind] = Archive.select_x()
#print(xi)
#[xj, ind] = coa.nextsol(xi, Problem, paramenters)
#print(xj)



coa.Run(Problem, archive, paramenters)

#archive.save_archive(name="zdt3")
#paramenters.save_results(name="zdt3")

if Problem.Nof <= 2:
    fig2, axs = plt.subplots()
    plt.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1])
    plt.show()
else:
    fig2 = plt.figure()
    axs = fig2.add_subplot(projection='3d')
    axs.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1],archive.FobjValues[:,2], marker='X')
    plt.show()