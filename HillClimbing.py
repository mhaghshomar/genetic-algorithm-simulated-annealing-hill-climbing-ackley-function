import matplotlib.pyplot as plt
import random
import math


x, y = [random.uniform(-100, 100), random.uniform(-100, 100)]
totalSteps = 200

def AckleyFunction(x, y):
    return -20 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
        0.5 * (math.cos(math.pi * 2 * x) + math.cos(math.pi * 2 * y))) + math.exp(1) + 20

def getNeighbours(x, y):
    neighbours = {}
    for i in range(-5, 6):
        for j in range(-5, 6):
            neighbours[(x + i, y + j)] = AckleyFunction(x + i, y + j)
    return neighbours

def getBestNeighbour(neighbours):
    key_list = list(neighbours.keys())
    val_list = list(neighbours.values())
    best = 1000
    for i in val_list:
        if i < best:
            best = i
            position = val_list.index(i)
    return key_list[position]

def hillClimbing(x, y):
    a = []
    b = []
    step = 1
    while step < totalSteps:
        neighbours = getNeighbours(x, y)
        bestNeighbour = getBestNeighbour(neighbours)
        if bestNeighbour != (x, y):
            (x, y) = bestNeighbour
        else:
            break
        a.append(step)
        b.append(AckleyFunction(x, y))
        step += 1
    print('f({},{}) = {}'.format(x, y, AckleyFunction(x, y)))

    plt.plot(a, b)
    plt.xlabel('Steps')
    plt.ylabel('Ackley value')
    plt.show()

hillClimbing(x, y)