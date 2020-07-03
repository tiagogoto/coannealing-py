import numpy as np
import math


def peturb(x, delr, e, C):
    aux=0
    nov=x.size
    xj=x
    ind=np.random.randint(low=0,high=nov, size=1)
    print("o indice sorteado:",ind)
    m=C[ind]
    cont=0
    print("o valor de m= ", m)
    while cont<m:
        aux=aux+(np.random.rand()-0.5)
        cont=cont+1
    xj[ind]=x[ind]+1/C[ind]*aux*delr*e
    return xj, ind