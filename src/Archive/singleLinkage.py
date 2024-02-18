import numpy as np

def euclidean_distance(point_a, point_b):
    return np.sqrt(sum((point_a - point_b) ** 2))

def dist_matrix(Solutions):
  [num_of_sol, nov] = np.shape(Solutions)
  dist_mat =  np.zeros([num_of_sol, num_of_sol])
  for i in range(0, num_of_sol):
    for j in range(i + 1, num_of_sol):
      dist_mat[i][j] = euclidean_distance(Solutions[i], Solutions[j])
  return dist_mat

def sort_matrix(dist_mat):
  [lin, col] = np.shape(dist_mat)
  minvalue = 100000
  for i in range(0,lin):
    for j in range(i,col):
      if dist_mat[i, j] != 0 and dist_mat[i, j] < minvalue:
        minvalue = dist_mat[i,j]
        minarg = [i, j]
  return minarg

def sort_matrix_a(dist_mat, flag):
  [lin, col] = np.shape(dist_mat)
  minvalue = 100000
  for i in range(0,lin):
    for j in range(i,col):
      if dist_mat[i, j] != 0 and dist_mat[i, j] < minvalue:
        if flag[i] != 1 or flag[j] != 1:
          minvalue = dist_mat[i,j]
          minarg = [i, j]
  return minarg

def single_linkage_a(Solutions, Fobj, flag):
  dist = dist_matrix(Solutions)
  args = sort_matrix_a(dist, flag)
  if any(flag[args] == 1):
    if flag[args[1]] != 1:
      return args[1]
    else:
      return args[0]
  else:
    return args[0]
  
def single_linkage_b(Solutions, Fobj, flag):
  dist = dist_matrix(Solutions)
  args = sort_matrix(dist)
  return args[1] 





