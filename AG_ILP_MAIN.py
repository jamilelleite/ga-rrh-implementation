import numpy as np
import AG_ILP_POPULATION as Population
import random
import AG_ILP_DATA1 as data1
import AG_ILP_DATA2 as data2
import AG_ILP_DATA3 as data3


def main(data):
    def create_popul(size_pop, number_generations, mut_rate, nodes, users, SC, poss_impla_SC, taxa, PRB, QoS):
        popul = Population.Population(size_pop, number_generations, mut_rate, nodes, users, SC, poss_impla_SC, taxa, PRB, QoS)

        popul.calc_fitness()

        return popul


    def draw(population):
        for _ in range(population.number_generations):
            population.natural_selection()
            population.generate()
            population.calc_fitness()
            population.get_best()


    size_pop, number_generations, mut_rate, nodes, users, SC, poss_impla_SC, taxa, PRB, QoS = data.size_pop, data.number_generations, data.mut_rate, data.Node, data.User, data.SC, np.array(data.Implant), np.array(data.Taxa), data.PRB, data.QoS

    popul = create_popul(size_pop, number_generations, mut_rate, nodes, users, SC, poss_impla_SC, taxa, PRB, QoS)

    draw(popul)

    arquivo = open("ResultadosAG.txt", "a")
    arquivo.write('\n')
    arquivo.write('\n')
    arquivo.write('\nRRHs implantadas:\n')
    # arquivo.writelines(str(popul.best.SC_implantadas))
    arquivo.write(str(np.sum(popul.best.SC_implantadas)))

    # print('\nSC RRHs implantadas:')
    # print(popul.best.SC_implantadas)
    # print(np.sum(popul.best.SC_implantadas))

    # print('\nSC que atende cliente:')
    # print(popul.best.Client)

    # print('\nPRBs pra cada cliente:')
    # print(popul.best.ClientPRB)

# main(data1)

# main(data2)

main(data1)

# main(data2)

# main(data3)