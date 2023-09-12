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
  def InitArchive(self, Problem, Paramenters):
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
  def Insert(self, xi, FobjValue):
    self.FobjValues = np.vstack((self.FobjValues, FobjValue))
    self.Solutions = np.vstack((self.Solutions, xi))
  #check if the solutions belong to the Archive
  def CheckIfBelongs(self, xi):
    count = 0
    IsBelongs = False
    Index = 0
    for x in self.Solutions:
      if np.array_equal(x, xi):
        Index = count
        IsBelongs = True
      count +=1
    return IsBelongs, Index
  # remove an solution from Archive
  def RemoveSolution(self, Index):
    np.delete(self.Solutions, Index)
    np.delete(self.FobjValues, Index)
  # clusterization algorithm function
  def Clusterization(self, Paramenters):
      f1max =
      f
      while :
