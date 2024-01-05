from src.Archive.GiftWrapping import GiftWrapping2D, GiftWrapping3D
#from singleLinkage import Single_Linkage
import scipy.cluster.hierarchy as shc

class Archive:
  def __init__(self, Problem, Paramenters):
    self.SL = Paramenters.SL
    self.HL = Paramenters.HL
    self.Nof = Problem.Nof
    self.Nov = Problem.Nov
    self.pop = 0
    self.FobjValues = np.empty(0,self.Nof)
    self.Solutions = np.empty(0, self.Nov)

  def size(self):
    [Row, Col] = np.shape(self.Solutions)
    return Row
  
  def init_archive(self, Problem, Paramenters):
    count = 0
    aux = np.empty(self.Nov)
    while count <= self.SL:
      for i in range(0,self.Nov):
        aux[i] = Problem.minv[i] + np.random.rand() * (Problem.maxv[ind] + Problem.minv[ind])
      aux2 = Problem.restriction(aux)
      if aux2:
        self.Solutions = np.vstack((self.Solutions, aux))
        self.FobjValues = Problem.evaluate(aux)
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
  def domination(solution_a, solution_b):
    equal = 0
    less = 0
    larger = 0
    for i in range(self.nof):
      if solution_a[i] < solution_b[i]:
        less += 1 
      elif abs(solution_a[i] - solution_b[i]) < 10^(-3):
        equal = equal + 1
      else:
        larger += 1
    if (less + equal ) == self.nof  and larger == 0:
      dominance = 1
    elif (larger + less ) == nof and equal == 0:
      dominance = 0
    else:
      dominance = 0
    return dominance

  def remove_remaining(to_remove, flag):
    [lin, col] = shape(self.Solutions)
    count = 0
    stop = 0
    while count < lin and stop != 1:
      for i in range(0,lin):
        aux = 0
        if i != count and self.domination == 1:
          dsfsdfsd
          
  def clusterization(self, Paramenters):
    [qtd, nof] = np.shape(self.Solutions)
    flag = np.empty([0])
    ## find the extrme of pareto front and slutions that belongs to the convexhull 
    fmax = np.zeros(nof)
    fmax[0:3] = 0
    fmaxarg = np.zeros(3)
    new_convhull = np.empty([0, nof])
    # get solutions in convehull 
    if nof < 3:
      convhull = GiftWrapping2D(self.FobjValues)
    else:
      convhull = GiftWrapping3D(self.FobjValues)
    [num_hull, col_hull] = np.shape(convhull)
    for ii in range(0,num_hull):
      for jj in range(0,num_hullhull):
        if ii != jj:
          if self.domination(convhull[ii], convhull[jj]):
            new_convhull = np.vstack((new_convhull, convhull[ii]))


    # make a flag to teh solutions in the extreme of pareto front and solution that belongs to convhull
    for i in range(0,qtd):
      check_status = 0
      for j in range(nof):
        if self.FobjValues[i,j] > fmax[j]:
          fmax = self.FobjValues
          fmaxarg[j] = i
        if self.FobjValues[i][j] == new_convhull[j]:
          check_status += 1
      if check_status == 3:
        flag[i] = 1
    flag[fmaxarg] = 1
    # remove solution until reached HL
    to_remove = qtd - self.HL
    count  = 0
    while count != to_remove:
      [lin, col] = np.shape()
      for i in range(0,lin):
        if count != i:
          if self.domination(sol, solb):


    
    '''
    [ ] develoopment of convhull only the  solution on pareto front 
    [ ] 
    [ ]
    [ ]   
    '''



      # first step  remove solutions out of shell

      # second step remove solutions from outer shell

      # third step remov the other solutions

