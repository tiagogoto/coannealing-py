import numpy as np
import math
from scipy.special import expit
import matplotlib.pyplot as plt


def fobj(x):
    col = np.size(x)
    aux = 0
    sol = 0
    for i in range(0, col):
        aux = aux+x[i]**2
    sol = aux
    print("valor de sol na função", sol)
    return sol


def peturb(x, C):
    delr = 10
    ei = 1
    nov = np.size(x)
    select = np.random.randint(low=0, high=nov, size=1)
    aux = 0
    cont = 0
    xj = np.zeros(nov)
    while (cont < C[select]):
        aux = aux + (np.random.rand() - 0.5)
        cont = cont+1
    for i in range(0, nov):
        if i == select:
            xj[i] = x[i] + delr * ei * aux/C[i]
        else:
            xj[i] = x[i]
    return xj, select


def SA(Tmax, Tmin, alpha, N, nov):
    temp = Tmax
    C_i = np.ones(nov)
    temperature = np.empty(0)
    Fun = np.empty(0)
    xi = np.random.rand(nov)*20
    soli = fobj(xi)
    print("valor de soli=", soli)
    xj = np.zeros(nov)
    solj = 0
    dE = 0
    while (temp > Tmin):
        for i in range(N):
            [xj, select] = peturb(xi, C_i)
            solj = fobj(xj)
            print("valor de solj", solj)
            dE = solj-soli
            print("valor de dE=", dE)
            P = expit(-dE/temp)
            r = np.random.rand(1)
            if (dE <= 0):
                xi = xj
                soli = solj
                # print("solução aceita", solj)
                C_i[select] = C_i[select]-1
                if (C_i[select] <= 0):
                    C_i[select] = 1
            elif (r < P):
                xi = xj
                soli = solj
                # print("solução aceita", solj)
                C_i[select] = C_i[select]-1
                if (C_i[select] <= 0):
                    C_i[select] = 1
            else:
                xi = xi
                soli = soli
                if (C_i[select] < 22):
                    C_i[select] = C_i[select]+1
        temperature = np.append(temperature, temp)
        Fun = np.append(Fun, soli)
        temp = temp*alpha
    print(temperature)
    plt.plot(temperature, Fun)
    plt.title("Z vs temperature", fontsize=20, fontweight='bold')
    plt.xlabel("Temperature", fontsize=18, fontweight='bold')
    plt.ylabel("Valor da função", fontsize=18, fontweight='bold')
    plt.xlim(100, 0)
    plt.xticks(np.arange(
        min(temperature), max(temperature), 10),
        fontweight='bold')
    plt.yticks(fontweight='bold')
    plt.show()
    return soli, xi


[sol, x] = SA(100, 0.001, 0.85, 60, 3)
print("O menor valor da função", sol)
print("a melhor solução é:", x)
