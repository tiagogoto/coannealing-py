import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
import src.Benchmark as benchmark
#import src.Coannealing as Coannealing
import src.Archive.Archive as Archive
from src.Archive.GiftWrapping import GiftWrapping2D
import src.Paramenters as Paramenters


Problem  = benchmark.get_problem(name="ZDT1", NumberofFunction=2, NumberofVariable = 30)
paramenters = Paramenters.Paramenters(Problem, N=1000, Tmax = 300, Tmin=0.000001, SL= 200, HL=70) 
archive = Archive.Archive(Problem, paramenters)

archive.init_archive(Problem)

print(np.shape(archive.FobjValues))

'''
for values in archive.FobjValues:
    print(values)
'''

convhull = GiftWrapping2D(archive.FobjValues)

points = archive.points_on_hull(convhull)

print("shape", np.shape(convhull))
print("após eliminar")
print(np.shape(points))
print(points)
#fig1 = plt.scatter(points[:,0], points[:,1])
print("Clusterização")
fig, axs = plt.subplots(3)
fig.suptitle("antes da clusterização e depois")
axs[0] = plt.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1])
archive.clusterization()
axs[1] = plt.scatter(archive.FobjValues[:, 0], archive.FobjValues[:,1], color='r')
plt.show()
print(np.shape(archive.FobjValues))


