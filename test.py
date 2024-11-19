import matplotlib.pyplot as plt
import src.Benchmark as benchmark
import src.Archive.Archive as Archive
import src.Paramenters as Paramenters
from src.Coannealing import Coannealing

Problem  = benchmark.get_problem(name="zdt4")
paramenters = Paramenters.Paramenters(Problem, N=1000, Tmax = 200, Tmin=0.00000001, SL= 200, HL=100,strategy=2, alpha=0.95) 
archive = Archive.Archive(Problem, paramenters)
coa = Coannealing(paramenters)



coa.Run(Problem, archive, paramenters)


if Problem.Nof <= 2:
    fig2, axs = plt.subplots()
    plt.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1])
    plt.show()
else:
    fig2 = plt.figure()
    axs = fig2.add_subplot(projection='3d')
    axs.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1],archive.FobjValues[:,2], marker='X')
    plt.show()
