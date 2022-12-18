import numpy as np
import AG_ILP_DNA as DNA
import random
# import AG_ILP_DATA as data

class Population:
    def __init__(self,  size_pop, number_generations, mut_rate, Nodes, Users, SC, poss_impla_SC, Taxa, PRB, QoS):
        self.N = Nodes
        self.U = Users
        self.world_record = 0
        self.best = 0
        self.size_population = size_pop
        self.population = []
        self.number_generations = number_generations
        self.mating_pool = []
        self.mut_rate = mut_rate
        for _ in range(self.size_population):
            self.population.append(DNA.DNA(Nodes, Users, SC, poss_impla_SC, Taxa, PRB, QoS))
                                                   
    def calc_fitness(self):
        for i in range(self.size_population):
            self.population[i].fitness_function()

    def natural_selection(self):
        max_fitness = 0
        self.matingPool = []

        for i in range(self.size_population):
            if self.population[i].fitness_score > max_fitness:
                max_fitness = self.population[i].fitness_score

        #fitne ja deve ter sido calculado
        for i in range(self.size_population):
            n_pool = int((self.population[i].fitness_score * 1000)/max_fitness)
            for _ in range(n_pool):
                self.matingPool.append(self.population[i])

    def generate(self):
        size_mating_pool = len(self.matingPool)
        for i in range(self.size_population):
            a = random.randrange(0, size_mating_pool)
            b = random.randrange(0, size_mating_pool)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mut_rate)
            self.population[i] = child

    def get_best(self):
       for i in range(self.size_population):
            if self.population[i].fitness_score > self.world_record:
                # index_world_record = i
                self.world_record = self.population[i].fitness_score
                self.best = self.population[i]


# popul = Population(data.size_pop, data.number_generations, data.mut_rate, data.Node, data.User, data.SC, data.Implant, data.Taxa, data.PRB, data.QoS)

# popul.calc_fitness()

# popul.get_best()

# popul.natural_selection()

# popul.generate()





        
