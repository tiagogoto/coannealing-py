import numpy as np

def euclidean_distance(point_a, point_b):
    return np.sqrt(sum((point_a - point_b) ** 2))


def Single_Linkage(solutions, fobjvalues):
    [num_of_sol, nof] = np.shape(solutions)
    count = 0
    min_dist = 1000000 
    dist_matrix = np.zeros([num_of_sol, num_of_sol])
    while count < num_of_sol:
        for i in range(0,num_of_sol):
            if i == count:
                dist_matrix[count][i] = None
            else:
                dist_matrix[count][i] = euclidean_distance(solutions[count], solutions[i])
                if dist_matrix[count][i] < min_dist:
                    min_dist = dist_matrix[count][i]

    


    return list_cluster
