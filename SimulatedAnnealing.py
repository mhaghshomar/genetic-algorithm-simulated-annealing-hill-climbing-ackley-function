import matplotlib.pyplot as plt
import random
import math


x, y = [random.uniform(-10, 10), random.uniform(-10, 10)]
totalSteps = 200
temperature = 1


def AckleyFunction(x, y):
    return -20 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
        0.5 * (math.cos(math.pi * 2 * x) + math.cos(math.pi * 2 * y))) + math.exp(1) + 20

def getBestNeighbour(x, y):
    curr_value = AckleyFunction(x, y)
    i, j = 0, 0
    while not(i != 0 or j != 0):
        i = random.randint(-5, 5)
        j = random.randint(-5, 5)
    neighbour_value = AckleyFunction(x + i, y + j)
    if neighbour_value < curr_value:
        curr_state = [x + i, y + j]
    else:
        if random.random() <= math.exp(float((curr_value - neighbour_value) * 2 / temperature)):
            curr_state = [x + i, y + j]
        else:
            curr_state = [x, y]
    return curr_state

def SimulatedAnnealing(temperature, x, y):
    a = []
    b = []
    step = 1
    while step < totalSteps:
        declineRate = temperature / step
        (x, y) = getBestNeighbour(x, y)
        temperature = temperature - declineRate
        a.append(step)
        b.append(AckleyFunction(x, y))
        step += 1

    print('f({},{}) = {}'.format(x, y, AckleyFunction(x, y)))

    plt.plot(a, b)
    plt.xlabel('Steps')
    plt.ylabel('Ackley value')
    plt.show()

SimulatedAnnealing(temperature,x, y)
