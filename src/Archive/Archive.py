import numpy as np
import scipy.cluster.hierarchy as shc
from datetime import datetime
from src.Archive.GiftWrapping import GiftWrapping2D, GiftWrapping3D
from src.Archive.singleLinkage import single_linkage_a, single_linkage_b


class Archive:
  def __init__(self, Problem, Paramenters):
    self.SL = Paramenters.SL
    self.HL = Paramenters.HL
    self.Nof = Problem.Nof
    self.Nov = Problem.Nov
    self.pop = 0
    self.FobjValues = np.empty([0,self.Nof])
    self.Solutions = np.empty([0, self.Nov])

  def size(self):
    [Row, Col] = np.shape(self.Solutions)
    return Row
  
  def init_archive(self, Problem):
    count = 0
    aux = np.empty(self.Nov)
    while count < self.SL:
      for i in range(0,self.Nov):
        aux[i] = Problem.minv[i] + np.random.rand() * (Problem.maxv[i] + Problem.minv[i])
      aux2 = Problem.restriction(aux)
      if aux2:
        self.Solutions = np.vstack((self.Solutions, aux))
        self.FobjValues = np.vstack((self.FobjValues,Problem.evaluate(aux)))
        count += 1
  # insert a new solution

  def insert(self, xi, FobjValue):
    self.FobjValues = np.vstack((self.FobjValues, FobjValue))
    self.Solutions = np.vstack((self.Solutions, xi))
  #check if the solutions belong to the Archive

  def check_if_belongs(self, xi):
    count = 0
    is_belongs = False
    index = 0
    for x in self.Solutions:
      if np.array_equal(x, xi):
        Index = count
        is_belongs = True
      count +=1
    return is_belongs, index
  
  # remove an solution from Archive
  def remove_Solution(self, Index):
    np.delete(self.Solutions, Index)
    np.delete(self.FobjValues, Index)
  # clusterization algorithm function
    
  def domination(self, solution_a, solution_b):
    equal = 0
    less = 0
    larger = 0
    for i in range(self.Nof):
      if solution_a[i] < solution_b[i] or abs(solution_a[i] - solution_b[i]) < 10**(-3) :
        less += 1 
      elif abs(solution_a[i] - solution_b[i]) < 10^(-6):
        equal = equal + 1
      else:
        larger += 1
    if (less + equal ) == self.Nof and larger== 0:
      dominance = 1  # if return 1 solution_a dominate solution b
    elif (larger + less ) == self.Nof and equal == 0:
      dominance = 0
    else:
      dominance = 0 # if return 0, solution_a is dominated or no nondominate
    return dominance

  def remove_bad(self, flag):
    count = 0
    stop = 0
    to_remove = self.size() - self.HL
    #print(f"a serem removido: {to_remove}")
    remove_index = np.empty(0, dtype=int)
    while count < self.size() and stop == 0:
      for i in range(0,self.size()):
        if count != i and flag[i] == 0:
          if self.domination(self.FobjValues[count], self.FobjValues[i]):
            remove_index = np.append(remove_index, i)
      if np.size(np.unique(remove_index)) >= self.size():
        stop = 1
      #print("count:",count)
      #print("remove list size:", np.size(np.unique(remove_index)))
      count += 1
      
    self.FobjValues = np.delete(self.FobjValues, remove_index, axis=0)
    self.Solutions = np.delete(self.Solutions, remove_index, axis=0)

    
  def points_on_hull(self, convhull):
    [lin, col] = np.shape(convhull)
    #print(f"valor da lin: {lin} valor de col{col}")
    count = 0
    flag = np.empty(0, dtype=int)
    index_points = np.empty(0, dtype=int)
    while count < lin:
      for i in range(0,lin):
        #print(self.domination(convhull[count], convhull[i]))
        if count != i:
          if self.domination(convhull[count], convhull[i]):
            flag = np.append(flag, i)
            #print(f"{count} domina {i}")
          
      count += 1
    #print(flag)
    convhull = np.delete(convhull, flag, axis=0)
    points = convhull.copy()
    return points
#
# Clusterização
#

  def clusterization(self):
    flag = np.zeros(self.size(), dtype=int)
    fmax = np.zeros(self.Nof)
    fmaxarg = np.zeros(3, dtype=int)
    # get solutions on the convexhull
    self.remove_bad(flag)
    if self.Nof < 3:
      convhull = GiftWrapping2D(self.FobjValues)
    else:
      convhull = GiftWrapping3D(self.FobjValues) 
    convhull_PF = self.points_on_hull(convhull)
    # Segundo o artigo as prioridades de remoção:
    
    
    for i in range(self.Nof):
      fmax[i] = self.FobjValues[:, i].max()
      fmaxarg[i] = self.FobjValues[:, i].argmax()
    flag[fmaxarg] = 1
    
    for fobj, index in zip(self.FobjValues, range(0,self.size())):
      if fobj.tolist() in convhull_PF.tolist():
        flag[index] = 1

        
    qtd_flag =  np.count_nonzero(flag == 1)
    while self.size() > self.HL and self.size() >= qtd_flag:
      arg = single_linkage_a(self.Solutions, self.FobjValues, flag)
      self.FobjValues = np.delete(self.FobjValues, arg, axis=0)
      self.Solutions = np.delete(self.Solutions, arg, axis=0)
    stop = 0
    while self.size() > self.HL and stop < 100000:
      print("remoção entre todas")
      arg = single_linkage_b(self.Solutions, self.FobjValues, flag)
      self.FobjValues = np.delete(self.FobjValues, arg, axis=0)
      self.Solutions = np.delete(self.Solutions, arg, axis=0)
      stop += 1
   
      
  def select_x(self):
    rng = np.random.default_rng()
    ind = rng.integers(0,self.size(), dtype=int)
    aux = self.Solutions[ind].copy()
    aux2 = self.FobjValues[ind].copy()
    return aux, aux2, ind
  
  def maxmin(self):
    R = np.zeros(self.Nof)
    for i in range(self.Nof):
      R[i] = self.FobjValues[:, i].max() - self.FobjValues.min()
    return R
  
  def save_archive(self, name):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    nameF = f"fobj-{name}-{dt_string}-.txt"
    nameS = f"sol-{name}-{dt_string}-.txt"
    np.savetxt(nameF, self.FobjValues, delimiter=',')
    np.savetxt(nameS, self.Solutions, delimiter=',')
  

      # first step  remove solutions out of shell

      # second step remove solutions from outer shell

      # third step remov the other solutions

