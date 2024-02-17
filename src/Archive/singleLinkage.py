import numpy as np

def euclidean_distance(point_a, point_b):
    return np.sqrt(sum((point_a - point_b) ** 2))

def single_linkage_a(solutions, flag):


def single_linkage_b(solutions):
  [num_of_sol, nof] = np.shape(fobjvalues)
  dist_matrix =  np.zeros([num_of_sol, num_of_sol])
  for i in range(0, num_of_sol):
    for j in range(i + 1, num_of_sol):
      dist_matrix[i][j] = euclidean_distance(solutions[i], solutions[j])
  return dist_matrix

 def sort_matrix(dist_matrix):
  [lin, col] = np.shape(dist_matrix)
  minvalue = 100000
  for i in range(0,lin):
    for j in range(i,col):
      if dist_matrix[i, j] != 0 and dist_matrix[i, j] < minvalue:
        minvalue = dist_matrix[i,j]
        minarg = [i, j]
  return minarg

def 

