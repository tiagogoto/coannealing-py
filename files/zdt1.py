import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import expit
from coaf import isdomina, iarch, newsol, maxmin, delws, clust, inc, maxdom, coannealing


def fobj(x):
    sol = np.zeros(2)
    sol[0] = x[0]
    aux = 0
    for i in range(1,29):
        aux = aux +x[i]
    g = 1 + 9 / 29 * aux
    h = 1 - (sol[0] / g)**(1 / 2)
    sol[2] = g * h
    return sol

def res(x):
    
    re = True

    return re
def isdomina(x_i, x_j):
    f_i = function(x_i)
    f_j = function(x_j)
    nof = f_j.size
    flagless = 0
    flagequal = 0
    aux = None
    for i in range(nof):
        if f_i[i] < f_j[i]:
            flagless = flagless + 1
        elif f_j[i] == f_i[i]  and flagless > 0:
            aux = True
    else:
        aux = False
    return aux

def iarch(HL, SL, nov, xmax, xmin):
    x_j = np.empty([nov])
    archive = np.empty([0, nov])
    x_i = np.random.rand(nov)
    lines = 0
    r = 0
    while lines < (SL * 2):
        for i in range(0, nov):
            x_j[i] = np.random.uniform(low = xmin[i], high = xmax[i], size = None)
            if (res(x_j)) and isdomina(x_i, x_j) or r > 20:
                archive = np.vstack([archive, x_j])
                r =0
                lines = lines + 1
            else:
                r = r + 1
    return archive


def newsol(x_i, C, xmax, xmin):
    nov=1
    x_j=0
    es=0
    delr=10
    while es==0:
        rand=np.random.rand()
        u=0
        for i in range(C):
            u=u+np.random.uniform(high=0.5, low=-0.5, size=None)
        delta=u/C*delr*np.random.choice([-1,1])
        x_j=x_i+delta
        if x_j>xmax:
            x_j=xmax
        if x_j<xmin:
            x_j=xmin
        if res(x_j):
            es=1
        else:
            es=0
    return x_j


def maxmin(sol):
    nof=sol.shape[1]
    R=np.empty(nof)
    for i in range(0,nof):
        R[i]=max(sol[i])-min(sol[i])
    return R 

def delws(archive, sol, nof):
    nov=archive.shape[1]
    newarchive=np.empty([0,nov])
    size=archive.shape[0]
    lines=0
    flag=np.empty(archive.shape[0])
    #sol=np.empty([archive.shape[0], nof])
    #for i in range(archive.shape[0]):
        #sol[i]=function(archive[i])
    while lines<size:
        for i in range(0,size): 
            if lines != i:
                cont=0
                k=0
                for col in range(0,nof): #verifica se é dominado ou não
                    if sol[lines][col]<sol[i][col]:
                        cont=cont+1
                    else:
                        k=k+1
                if k==2:
                    flag[lines]=False
                    break
                else: 
                    flag[lines]=True
        lines=lines+1
    for l in range(archive.shape[0]):
        if flag[l]:
             newarchive=np.vstack([newarchive, archive[l]])
    return newarchive

def clust(size, archive):
    nof=archive.shape[1]
    while archive.shape[0]>size:
        linhas=archive.shape[0]
        mm=np.empty(linhas)
        deli=0
        for u in range(1,linhas):
            mm[u-1]=np.sqrt((archive[u-1]-archive[u])**2)
        diff=800
        ind=0
        for i in range(0, mm.size):
            if mm[i]<diff:
                diff=mm[i]
                ind=i
        #ind=np.argmin(mm)
        if ind!=0 and ind!=(mm.size-1):
            if mm[ind+1]<= mm[ind-1]:
                deli=ind+1
            elif mm[ind-1]<=mm[ind+1]:
                deli=ind
        elif ind==(mm.size-1):
            #lista=np.append(lista, ind-1)
            deli=ind-1
        else:
            #lista=np.append(lista, ind+1)
            deli=ind+1  
        archive=np.delete(archive, deli, axis=0)   
            
    return archive

def inc(x, archive):
    aux=None
    for i in range(archive.shape[0]):
        j=0
        for col in range(0,archive.shape[1]):
            if x[col] == archive[i][col]:
                j=j+1
        if j == archive.shape[1]:
            aux = True
            break
        else:
            aux=False
    return aux

def maxdom(sola, solarchive, nof, R):
    aux2 = 0
    aux = np.ones(solarchive.shape[0])
    for i in range(solarchive.shape[0]):
        for col in range(nof):
            if sola[col] == solarchive[i][col]:
                aux[i] = 1
            elif sola[col] < solarchive[i][col]:
                aux[i] = 0
                break
            else:
                aux[i] = aux[i] * (sola[col] - solarchive[i][col])*R[col]
    aux2 = np.amax(aux)
    return aux2

def coannealing(Tmax, Tmin, N, alpha, SL, HL, nof, nov, xmax, xmin):
    archive = iarch(HL, SL, nov,xmax, xmin)
    #archive=reo(archive,nov)
    ale = np.random.choice(np.arange(archive.shape[0]))
    x_i = archive[ale]
    temp = Tmax
    r = 0
    max_r = 10
    C = 1
    while temp>Tmin:
        for ciclo in range(N):
            x_j = newsol(x_i, C, xmax, xmin)
            solarchive = np.zeros([archive.shape[0], nof])
            soli = function(x_i)
            solj = function(x_j)
            #print(solj)
            for i in range(archive.shape[0]):
                solarchive[i] = function(archive[i])
            R = maxmin(solarchive)
            deltaE = maxdom(solj, solarchive, nof, R) - maxdom(soli, solarchive, nof, R)
            p = np.random.rand()
            prob = expit(-deltaE/temp)
            if deltaE <= 0 or p < prob:
                x_i = x_j
                soli = solj
                aux = maxdom(solj,solarchive,nof,R)
                C = C + 1
                if aux <= 0:
                    archive=np.vstack([archive, x_j])
                    solarchive=np.vstack([solarchive, solj])
                    #print("Adicionado")
                    if archive.shape[0]>SL:
                        archive=delws(archive, solarchive, nof)
                        archive=clust(HL, archive)
                        #print("Adicionado")
                        if inc(x_i,archive):
                            if r<max_r:
                                archive=np.vstack([archive, x_i])
                            else:
                                ale=np.random.choice(np.arange(archive.shape[0]))
                                x_i=archive[ale]
                                r=r+1
                        else:
                            r=0
            else:
                C=C-1
                if C<=0:
                    C=1
        temp=temp*alpha
        #print(archive.shape)
        #plotf(archive, 2,1)
        #archive=delws(archive, solarchive, nof)
    return archive

Tmax = 100
Tmin = 0.00001
N = 600
alpha = 0.85
SL = 100
HL = 50
nof = 2
nov = 30

xmin = np.zeros(30)
xmax = np.ones(30)
archive = coannealing(Tmax, Tmin, N, alpha, SL, HL, nof, nov, xmax, xmin)