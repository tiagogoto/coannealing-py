import numpy as np

def euclidean_distance(point_a, point_b):
    return np.sqrt(sum((point_a - point_b) ** 2))


def Single_Linkage(fobjvalues, solutions):
  [num_of_sol, nof] = np.shape(fobjvalues)
  dist_matrix =  np.zeros([num_of_sol, num_of_sol])
  for i in range(0, num_of_sol):
    for j in range(i + 1, i):
      dist_matrix[i][j] = euclidean_distance(solutions[i], solutions[j])
  return dist_matrix   

 def sort_matrix(dist_matrix):
  index_ind = np.empty([0])
  [lin, col] = np.shape(dist_matrix)
  for i in range(0,lin):
    for j in range(i,col):

  return index_ind


