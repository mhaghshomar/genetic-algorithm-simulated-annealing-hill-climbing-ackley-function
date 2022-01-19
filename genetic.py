import math
import random
import matplotlib.pyplot as plt

crossover_prob, mutation_prob = 0.75, 0.1
steps = 100
population_size, parent_size = 100, 10

def AckleyFunction(chromosome):
    x, y = chromosome
    return -20 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
        0.5 * (math.cos(math.pi * 2 * x) + math.cos(math.pi * 2 * y))) + math.exp(1) + 20

def creatPopulation():
    chromosomes = []
    for i in range(population_size):
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        chromosomes.append([x, y])
    return chromosomes


def crossover(parent_a, parent_b):
    x_a, y_a = parent_a
    x_b, y_b = parent_b
    childWithCrossover = [(x_a + x_b) * crossover_prob, (y_a + y_b) * crossover_prob]
    childNoCrossover = [(x_a + x_b) * (1 - crossover_prob), (y_a + y_b) * (1 - crossover_prob)]
    return childWithCrossover, childNoCrossover

def mutation(chromosome):

    if random.random() < mutation_prob:
        chromosome[random.choice([0, 1])] = random.uniform(-5, 5)

def naturalSelection(chromosomes, children):
    chromosomes = chromosomes[:int(population_size // 2)] + random.choices(children[:population_size],
                                                                          k = int(population_size // 2))
    return chromosomes


def geneticAlgorithem():
    step = 0
    a = []
    b = []
    chromosomes = creatPopulation()
    chromosomes.sort(key=AckleyFunction)
    for i in range(steps):
        parents = random.choices(chromosomes[:int(100 // 2)], k = parent_size)
        children = []
        for parent_a in parents:
            for parent_b in parents:
                child_a, child_b = crossover(parent_a, parent_b)
                mutation(child_a)
                mutation(child_b)
                children.append(child_a)
                children.append(child_b)
        children.sort(key=AckleyFunction)
        chromosomes = naturalSelection(chromosomes, children)
        chromosomes.sort(key=AckleyFunction)
        b.append(AckleyFunction(chromosomes[0]))
        step += 1
        a.append(step)

    print('f({},{}) = {}'.format(chromosomes[0][0], chromosomes[0][1], AckleyFunction(chromosomes[0])))

    plt.plot(a, b)
    plt.xlabel('Steps')
    plt.ylabel('Ackley value')
    plt.show()


geneticAlgorithem()