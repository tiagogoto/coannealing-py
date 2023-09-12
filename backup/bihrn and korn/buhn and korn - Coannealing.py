import math
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f1(x,y): ## função a ser otimizado 1
    obj = 4*x**2+y**2
    return obj
def f2(x,y): ##função a ser otimizado 2
    obj = (x-5)**2+(y-5)**2
    return obj
def g1(x,y):
    g=(x-5)**2+y**2
    if g <=25:
        aux=True
    else:
        aux = False
    return aux
def g2(x,y):
    g=(x-8)**2+(y+3)**2
    if g>=7.7:
        aux=True
    else:
        aux=False
    return aux
xg=np.linspace(0, 5,num=100)
yg=np.linspace(0, 3,num=100)

plt.plot(f1(xg,yg),f2(xg,yg), color='b',linewidth=2.5)
plt.xlabel("f_1(x,y)", fontsize=13,fontweight='bold')
plt.ylabel("f_2(x,y)",fontsize=13,fontweight='bold')
plt.title("Fronte de pareto",fontsize=15,fontweight='bold')

def dominancia(fi,fj):
    
    if :
        res=True
    else:
        res=False
    return res   #se TRue a solução nova domina a solução anterior
def Ddomi_ab(x_i,y_i,x_j,x_j):
    obj=(f1(x_j,x_j)-f1(x_i,y_i))
def Ddim_avg():
    
    avg=
    return avg
#inicialização das variáveis
Tmax=1000
Tmin=0
HL=300
SL=15
N=300 #número domain search 
alpha= 0.85 # deaimento da temperatura ou fator de resfriamento
temp=Tmax
archive = []
#solução inicial 
x_i=0.1
y_y=0.5
C=1  #fator mudança de direção
phi=0.1  #fator de redução

while temp>Tmin:
    for i in range(N):
        x_j=x_i+C*phi*np.random.rand()
        y_j=y_i+C*phi*np.random.rand()
        #checagem de dominância 
        
        if 
        
    temp=temp*alpha


