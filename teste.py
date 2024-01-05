import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
import Benchmark
import src.Coannealing as Coannealing
import src.Archive.Archive as Archive
import src.Paramenters as Paramenters

Problem  = Benchmark.get_problem("ZDT1", 2)
paramenters = Paramenters() 
archive = Archive(Problem, paramenters)



