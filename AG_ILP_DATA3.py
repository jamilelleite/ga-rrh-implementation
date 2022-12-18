mut_rate = 0.1
size_pop = 100
number_generations = 100 #100

#//////////////////////////////////////////////////////////////////////////////////////////////////

#2x2MIMO
#800 usuários
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

Taxa = pd.read_excel(r'Dados\2x2MIMO\800 usuários\(iter1) (BBUs 27 24 14) 800 users 7x7 RRHs 64QAM MIMO2x2.xlsx', header=None)
Taxa = Taxa.values