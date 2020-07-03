import numpy as np
import math
import peturb



r=1
e=1
x=np.random.rand(1)
print(x)
C=np.ones(1)
print("valor de C=", C)
[xj, ins]=peturb.peturb(x,r,e,C)

print("C= ", C)
print("nova solução:")
print(xj)