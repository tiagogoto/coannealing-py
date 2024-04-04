import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import src.Archive.Archive as Archive
from src.Archive.GiftWrapping import GiftWrapping2D
import src.Paramenters as Paramenters
from src.Coannealing import Coannealing
import src.Benchmark as benchmark


Problem  = benchmark.get_problem(name="dtlz3", NumberofFunction=3, NumberofVariable = 12)
paramenters = Paramenters.Paramenters(Problem, N=100, Tmax = 200, Tmin=0.00000001, SL= 50, HL=10, alpha=0.95) 
archive = Archive.Archive(Problem, paramenters)
archive.init_archive(Problem)

print("tamanho do archive antes de remover")
print(archive.size())
print(archive.FobjValues)
flag = np.zeros(archive.size())
archive.remove_bad(flag)
print("valor após a remoção das ruins")
print(archive.size())


x=np.random.rand(30,3)
print("o tamanho do archive: \n", np.shape(archive.FobjValues))
convhull = GiftWrapping2D(archive.FobjValues)
print(convhull)
print("tamanho do convhull:")
print("convhull\n", np.shape(convhull))



convhull_PF = archive.points_on_hull(convhull) 
print(np.shape(convhull_PF))

figure1= plt.figure()
ax = figure1.add_subplot(projection='3d')
plt.scatter(archive.FobjValues[:,0], archive.FobjValues[:,1], archive.FobjValues[:,2], color='red')
plt.scatter(convhull[:,0], convhull[:,1], convhull[:,2], color='black')
ax.scatter(convhull_PF[:,0], convhull_PF[:,1],convhull_PF[:,2], color='green', marker = 'x')
plt.show()
