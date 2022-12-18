import numpy as np 
import random
import math 
# import AG_ILP_DATA as data 

class DNA:
    def __init__(self, Nodes, Users, SC, poss_impla_SC, Taxa, PRB, QoS, child=False): #taxa de mutacao, numero de pontos, numero de usuarios, numero maximo de SC, possiveis locais de implem. de SC, Taxa que o usuario j recebe da SC i utilizando 1 PRB, Total de PRBs por SC, Taxa minima aceita por cada usuario
        self.N = Nodes
        self.U = Users
        self.SC = SC
        self.poss_impla_SC = poss_impla_SC
        self.taxa = Taxa
        self.PRB = PRB
        self.QoS = QoS
        self.SC_implantadas = np.zeros([Nodes], dtype=bool)
        self.Client = np.zeros([Users, Nodes], dtype=bool)
        self.ClientPRB = np.zeros([Users, Nodes], dtype=int) #3 variaveis de decisao
        self.bonus = 2
        self.fitness_score = 0
        #seta valores da variavel apenas se nao for um filho
        if not child:
            #cria individuo com genes aleatorios de acordo com poss_impla_SC
            for i in range(self.N):
                if poss_impla_SC[i] == 1:
                    if random.randrange(100) < 50: 
                        self.SC_implantadas[i] = True
            #cria individuo Client aleatorio com apenas um SC selecionado para cada usuario (nao garante numero total de SC)
            for i in range(self.U):
                aux0 = np.where(poss_impla_SC == 1)[0]  # [0] para retornar apenas o array numpy, e nao a tupla 
                                                        #retorna novo array com indices onde valor == 1
                aux1 = random.randrange(aux0.size)      # escolhe aleatoriamente um dos indices do novo array
                aux2 = aux0[aux1]                       #indice aleatorio com valor do array original == 1
                self.Client[i][aux2] = 1
            #cria individuo ClientPRB aleatorio com numeros de PRB onde individuo Client == 1
            #Da valor de PRB para usuarios atendidos pelas SC (nao garante PRBs maximos de cada SC nem Qos dos usuarios)
            for i in range(self.U):
                for j in range(self.N):
                    if self.Client[i][j] == True:
                        self.ClientPRB[i][j] = random.randint(1, self.PRB)
        
    def fitness_function(self):
        N = range(self.N)
        U = range(self.U)
        score = self.bonus
        down = False

        #Garante que vai ter no maximo SC Implantadas 
        sum = 0
        for j in N:
            sum += self.SC_implantadas[j]
        if sum <= self.SC:
            score *= 2
        else:
            down = True

        #Se o ponto nao for um possivel local para RRH ele nao pode ser escolhido para implantar uma RRH  
        for j in N:
            if not self.poss_impla_SC[j]:
                if not self.SC_implantadas[j]:
                    score *= 2
                else:
                    down = True

        #Cliente so pode ser atendido por SC implantadas
        for i in U:
            for j in N:
                if self.Client[i][j] <= self.SC_implantadas[j]:
                    score *= 2
                else:
                    down = True

        #Garante que o usuario i vai ser atendido. Exclusivamente por 1 SC
        for i in U:
            if np.sum(self.Client[i]) == 1:
                score *= 2
            else:
                down = True

        #Garante o minimo de PRBs para cada Usuario manter o QoS
        for i in U:
            for j in N:
                if self.ClientPRB[i][j] * self.taxa[i][j] >= self.QoS * self.Client[i][j]:
                    score *= 2 
                else:
                    down = True     

        #Garante que a SC nao vai dar mais PRBs do que tem 
        for j in N:
            if np.sum(self.ClientPRB[:,j]) <= self.PRB*self.SC_implantadas[j]:
                score *= 2
            else:
                down = True

        self.fitness_score = score

        if not down:  
            # #minimizar qnt  de PRBs distribuidas pelas SC (funcao objetivo)
            maxi = self.PRB*self.SC
            up = self.PRB*self.SC - np.sum(self.ClientPRB)
            porc0 = up/maxi
            # self.fitness_score *= (1 + porc)

        if not down:  
            # #minimizar qnt  de PRBs distribuidas pelas SC (funcao objetivo)
            maxi = self.PRB*self.SC
            up = self.PRB*self.SC - np.sum(self.ClientPRB)
            porc0 = up/maxi
            # self.fitness_score *= (1 + porc)

            # #minimizar numero de SC implantadas (funcao objetivo)          
            maxi = self.SC
            up = self.SC - np.sum(self.SC_implantadas)
            porc1 = up/maxi
            self.fitness_score *= (1 + porc1)            
            # self.fitness_score *= (1 + (porc0 + porc1)**1111)





    def crossover(self, partner):  #DNA partner
        N = range(self.N)
        U = range(self.U)

        child = DNA(self.N, self.U, self.SC, self.poss_impla_SC, self.taxa, self.PRB, self.QoS, True)
        
        #variavel de implantacao de SC pega metade dos pais
        midpoint = random.randrange(self.N)
        for j in N:
            if j < midpoint:
                child.SC_implantadas[j] = self.SC_implantadas[j]
            else:
                child.SC_implantadas[j] = partner.SC_implantadas[j]

        #variavel Client herda SC de qual usuario eh atendido de um dos pais, e variavel ClientPRB eh media do valor dos pais
        
        for i in U:
            try:
                aux0 = np.where(self.Client[i] == True)[0][0]
            except:
                child.Client[i] = partner.Client[i]
                child.ClientPRB[i] = partner.ClientPRB[i]
            else:
                try:
                    aux1 = np.where(partner.Client[i] == True)[0][0]   
                except:
                    child.Client[i] = self.Client[i]
                    child.ClientPRB[i] = self.ClientPRB[i]     
                else:
                    med = (self.ClientPRB[i][aux0] + partner.ClientPRB[i][aux1])/2
                    if random.randint(0,1) == 0:
                        child.Client[i][aux0] = True
                        child.ClientPRB[i][aux0] = med
                    else:
                        child.Client[i][aux1] = True
                        child.ClientPRB[i][aux0] = med

        return child



    def mutate(self, mut_rate):
        mut = mut_rate
        # mut = self.mut_rate

#testar crossover apenas pegando partes do array dos pais ou usar exception (complicado, achar outro metodo se cair nele)

        #muda um valor onde pode ser implementado SC da variavel de implantacao de SC
        if random.randint(0, 100) <= mut*100:
            aux0 = np.where(self.poss_impla_SC == 1)[0]  
            aux1 = random.randrange(aux0.size)
            aux2 = aux0[aux1]
            self.SC_implantadas[aux2] = not self.SC_implantadas[aux2]


        for i in range(self.U):
            #muda de qual SC usuario sera atendido
            if random.randint(0, 100) <= mut*100:
                try:
                    aux0 = np.where(self.Client[i] == True)[0][0]  
                except:
                    aux0 = random.randrange(self.N)
                    self.Client[i][aux0] = True
                else:
                    aux1 = random.randrange(self.N)
                    self.Client[i,[aux0,aux1]] = self.Client[i,[aux1,aux0]]
                    self.ClientPRB[i,[aux0,aux1]] = self.ClientPRB[i,[aux1,aux0]]

        for i in range(self.U):
        #muda a qnt de PRB recebidos
            if random.randint(0, 100) <= mut*100:
                try:
                    aux0 = np.where(self.ClientPRB[i] != 0)[0][0]  
                except:
                    pass
                else:
                    self.ClientPRB[i][aux0] = random.randint(1, self.PRB)


# dna1 = DNA(data.Node, data.User, data.SC, data.Implant, data.Taxa, data.PRB, data.QoS)
# dna1.fitness_function()

# dna2 = DNA(data.Node, data.User, data.SC, data.Implant, data.Taxa, data.PRB, data.QoS)
# dna2.fitness_function()

# child = dna1.crossover(dna2)
# child.mutate(data.mut_rate)