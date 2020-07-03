import numpy as np
import math
from scipy.special import expit

######## python function 

###### python objective funtion
def fobj(x):
    f1=x**2
    f2=(x-2)**2
    return sol
######## function generatio a newsolution
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
################# function to determine the R
def maxmin(sol):
    [line, col]=np.shape(sol)
    R=np.empty(col)
    for i in range(col):
        R[i]=max(sol[i])-min(sol[i])
    return R
################# functionm to determine de MaxDom
def MaxDom(soli, sarchive, R):
    [line, col]=np.shape(sarchive)
    aux=np.zeros(line)
    aux2=0
    for i in range(line):
        for j in range(col):
            if soli[j]<=sarchive[i, j]:
                aux[i]=0
            else
                aux[i]=aux[i]*(soli[j]-sarchive[i,j])*R[j]
    aux2=np.max(aux)
    return aux2
################ check function, this check if the solution is in the archive
def solin(x, arch):
    aux=None
    [line, col]=np.shape(arch)
    
    return aux
################ clustering function
def cluste(archive, solarchive, HL):
    [lines, nov] =
    [lines2, nof] = 
    newarch=np.zeros()


    return newarch, newsol

def coannealing(Tmax, Tmin, N, SL, HL, nov, nof, alpha):
    temp=Tmax

    while temp> Tmin:
        for i in range(0,N):
            [xi, ind]=peturbation(xi, r, e, C)
            solj=fobj(xi)
            R=maxmin(sarchive)
            DeltaE=MaxDom(solj, sarchive, R) - MaxDom(soli, sarchive, R)
            rand=np.random.rand()
            P=expit(-DeltaE/temp)
            if DeltaE<=0 or rand<P:
                xi=xj
                soli=solj
                aux=MaxDom(solj, sarchive, R)
                C[ind]=C[ind]-1
                if C[ind]<=0:
                    C[ind]=1             
                if aux<=0:
                    archive=np.vstack([archive, xj])
                    sarchive=np.vstack([sarchive, solj])
                    if archive.shape[0]>SL:
                        [archive, sarchive]=Clust(archive, sarchive, HL)
                        if xi
            else:
                if C[ind]<20:
                    C[ind]=C[ind]+1
        temp=temp*alpha
    return archive, sarchive


Tmax=100
Tmin=0.0001
N=300 #number of variable multipli peer 20
SL=100 
HL=50     
nov=1 #number of design variable in the optimization problem
nof=2 # number of function 
alpha=0.85  #alpha 
# Tmax, Tmin, N, SL, HL, nov, nof, alpha

[archive, sarchive]=coannealing(Tmax, Tmin, N, SL, HL, nov, nof, alpha)
#get archive and solarchive




    