import numpy as np
import scipy.cluster.hierarchy as shc
from src.Archive.GiftWrapping import GiftWrapping2D, GiftWrapping3D
#from singleLinkage import Single_Linkage


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
      if solution_a[i] < solution_b[i]:
        less += 1 
      elif abs(solution_a[i] - solution_b[i]) < 10^(-3):
        equal = equal + 1
      else:
        larger += 1
    if (less + equal ) == self.Nof  and larger == 0:
      dominance = 1  # if return 1 solution_a dominate solution b
    elif (larger + less ) == self.Nof and equal == 0:
      dominance = 0
    else:
      dominance = 0 # if return 0, solution_a is dominated or no nondominate
    return dominance

  def remove_remaining(self, to_remove, flag):
    [lin, col] = np.shape(self.Solutions)
    count = 0
    stop = 0
    while count < lin and stop != 1:
      for i in range(0,lin):
        aux = 0
        if i != count and self.domination == 1:
          dsfsdfsd
  def points_on_hull(self, convhull):
    [lin, col] = np.shape(convhull)
    count = 0
    flag = np.empty(0, dtype=int)
    index_points = np.empty(0, dtype=int)
    while count < lin:
      for i in range(0,lin):
        if self.domination(convhull[count], convhull[i]):
          flag = np.append(flag, i)
      count += 1
    #print(flag)
    points = np.delete(convhull, flag, axis=0)
    return points

  def clusterization(self):
    [qtd, nof] = np.shape(self.FobjValues)
    flag = np.zeros(qtd, dtype=int)
    ## find the extrme of pareto front and slutions that belongs to the convexhull 
    fmax = np.zeros(nof)
    fmax[0:nof] = 0
    fmaxarg = np.zeros(3, dtype=int)
    # get solutions in convehull 
    if nof < 3:
      convhull = GiftWrapping2D(self.FobjValues)
    else:
      convhull = GiftWrapping3D(self.FobjValues)
    ### até aqui ok
    convhull_PF = self.points_on_hull(convhull)   
    #print("convhull_PF, dentro da clusterizaçaõ", convhull_PF)
    # make a flag to teh solutions in the extreme of pareto front and solution that belongs to convhull
    for i in range(0,qtd):
      check_status = 0
      for j in range(nof):
        #print("f:" , self.FobjValues[i][j])
        #print("fmax", fmax[j])
        if self.FobjValues[i][j] > fmax[j]:
          fmax[j] = self.FobjValues[i, j]
          fmaxarg[j] = i
        #if self.FobjValues[i,j] == convhull_PF[j]:
          #check_status += 1
      if self.FobjValues[i,:].tolist() in convhull_PF.tolist():#check_status == 3:
        flag[i] = 1
    flag[fmaxarg] = 1
    
    # remove solution until reached HL
    to_remove = qtd - self.HL
    count  = 0
    stop = 0
    remove_index = np.empty(0, dtype=int)
    while count != to_remove and stop == 0:
      [lin, col] = np.shape(self.FobjValues)
      for i in range(0,lin):
        if count != i and flag[i] == 0:
          if self.domination(self.FobjValues[count], self.FobjValues[i]):
            remove_index = np.append(remove_index, i)
      if np.size(remove_index) >= to_remove or count >= qtd:
        stop = 1
      count += 1
    self.FobjValues = np.delete(self.FobjValues, remove_index, axis=0)
    self.Solutions = np.delete(self.Solutions, remove_index, axis=0)

  def clusterization2(self):
    flag = np.zeros(qtd, dtype=int)
    fmax = np.zeros(nof)
    fmaxarg = np.zeros(3, dtype=int)
    # get solutions on the convexhull
    if nof < 3:
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
    



  
  def select_x(self):
    rng = np.random.default_rng()
    ind = rng.integers(0,self.size(), dtype=int)
    aux = self.Solutions[ind].copy()
    aux2 = self.FobjValues[ind].copy()
    return aux, aux2, ind
  
  def maxmin(self):
    R = np.zeros(self.Nof)
    for i in range(self.Nof):
      R = np.zeros(self.Nof)
      R[i] = self.FobjValues[:, i].max() - self.FobjValues.min()
    return R
  
  

    

       


    
    '''
    [ ] develoopment of convhull only the  solution on pareto front 
    [ ] 
    [ ]
    [ ]   
    '''



      # first step  remove solutions out of shell

      # second step remove solutions from outer shell

      # third step remov the other solutions

