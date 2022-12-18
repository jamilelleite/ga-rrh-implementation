mut_rate = 0.1
size_pop = 100
number_generations = 100 #100

# SC = 6 #// Total de SmallCells.
# User = 6 #// Total de Usuarios.
# QoS = 1000 #// Taxa minima de cada usu�rio (100,0,Kbps)
# PRB = 500 #// Total de PRBs por SC
# Node = 6 #// Total de pontos que existe. Quanto menor o passo mais pontos tem. (Node = X * Y)

# Implant = [1, 1, 1, 1, 1, 1] # // Possiveis locais para Implantar SC (Passo 50,m)

# # // Taxa que o usu�rio j recebe da SC i utilizando 1 PRB 
# Taxa =  	[	[100, 100, 0, 0, 0, 0],
# 				[100, 0, 0, 0, 0, 0],
# 				[100, 0, 0, 0, 0, 0],
# 				[0, 100, 0, 0, 100, 0],
# 				[0, 100, 0, 0, 100, 0],
# 				[0, 100, 0, 0, 100, 0]]


#//////////////////////////////////////////////////////////////////////////////////////////////////

#2x2MIMO
#400 usuários
#7x7 RRHs
#int 1

import pandas as pd
import numpy as np

SC = 49 #// Total de SmallCells.
User = 400 #// Total de Usuarios.
QoS = 1000 #// Taxa minima de cada usu�rio (100,0,Kbps)
PRB = 500 #// Total de PRBs por SC
Node = 49 #// Total de pontos que existe. Quanto menor o passo mais pontos tem. (Node = X * Y)

Implant = np.ones(Node, dtype=int) # // Possiveis locais para Implantar SC (Passo 50,m)

Taxa = pd.read_excel(r'Dados\2x2MIMO\400 usuários\(iter1) (BBUs 47 2 37) 400 users 7x7 RRHs 64QAM MIMO2x2.xlsx', header=None)
# Taxa = pd.read_excel(r'Dados\2x2MIMO\400 usuários\(iter1) (BBUs 47 2 37) 400 users 7x7 RRHs 64QAM MIMO2x2.xlsx', header=None)
Taxa = Taxa.values

