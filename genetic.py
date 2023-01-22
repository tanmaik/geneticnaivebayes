# Tanmai Kalisipudi & Griff Boehnlein
# 1/23/23

from naive import naive
from random import random, choice
import sys
from tqdm import tqdm


POPULATION_SIZE = 100
NUM_CLONES =0
MUTATION_RATE = .2
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
NUM_GENERATIONS = 100

# Functions needed: 

# fitness(weights)
# generate_random_weights()
# generate_initial_population()
# rank_population()
# breed(mom, dad)


def fitness(strategy):
    return naive(strategy)

def generate_random_weights():
    return [random() for x in range(14)]

def init_population():
    return [generate_random_weights() for x in range(POPULATION_SIZE)]

def rank_population(population):
    strat_to_fitness = dict()
    for index, strategy in enumerate(population):
        strat_to_fitness[index] = fitness(strategy)
        ranked = sorted(strat_to_fitness.items(), key = lambda kv : (kv[1], kv[0]))
    return ranked[::-1]


def mutate(child):
    for index, weight in enumerate(child):
        if random() < MUTATION_RATE:
            child[index] = random()
    return child

def breed(mom, dad):
    child = []
    for i in range(len(mom)):
        if random() < .5:
            child.append(mom[i])
        else:
            child.append(dad[i])
    return child

def create_child(current_population):
    full_tourney = []
    while len(full_tourney) < (TOURNAMENT_SIZE * 2):
        toAdd = choice(current_population)
        if toAdd not in full_tourney:
            full_tourney.append(toAdd)
    tourney1 = full_tourney[:TOURNAMENT_SIZE]
    tourney2 = full_tourney[TOURNAMENT_SIZE:]
    tourney1.sort(key=lambda x:x[1])
    tourney2.sort(key=lambda x:x[1])
    tourney1 = tourney1[::-1]
    tourney2 = tourney2[::-1]
    parent1 = 0
    parent2 = 0
    for element in enumerate(tourney1):
        if random() <= TOURNAMENT_WIN_PROBABILITY:
            parent1 = popCurrent[element[0]]
            break
    for element in enumerate(tourney2):
        if random() <= TOURNAMENT_WIN_PROBABILITY:
            parent2 = popCurrent[element[0]]
            break
    if parent1 == 0:
        # print("couldn't find parent 1")
        parent1 = popCurrent[tourney1[0][0]]
    if parent2 == 0:
        # print("couldn't find parent 2")
        parent2 = popCurrent[tourney2[0][0]]
    child = breed(parent1, parent2)
    if random() < MUTATION_RATE:
        child = mutate(child)
    return child


popZero = init_population()
popCurrent = popZero

for x in range(NUM_GENERATIONS):
    newPop = []
    rankedPop = rank_population(popCurrent)
    for clone in range(NUM_CLONES):
        newPop.append(popCurrent[clone])
    while len(newPop) < POPULATION_SIZE:
        child = create_child(rankedPop)
        if child not in newPop:
            newPop.append(child)
        # print(newPop)
    popCurrent = newPop.copy()
    newPop = []
    print("Generation " + str(x) + " complete")
    rankedPop = rank_population(popCurrent)
    best_strategy = rankedPop[0][0]
    print("Best strategy accuracy: " + str(fitness(popCurrent[best_strategy])))