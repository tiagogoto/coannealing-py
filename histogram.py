#python 3.8!

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


#matriz=pd.read_csv('teste.csv', sep=',')
matriz =np.genfromtxt('teste.csv', delimiter=',')
print(matriz)
plt.hist(matriz, bins=10)
plt.show()
#matriz.hist(column='teste')