# Tanmai Kalisipudi & Griff Boehnlein
# 1/18/23

from naive import naive
from random import random
import sys
w_list = [random() for x in range(14)]
print(w_list)
naive(w_list)
sys.exit()

POPULATION_SIZE = 50
NUM_CLONES = 5
MUTATION_RATE = .2
TOURNAMENT_SIZE = 5
TOURNAMENT_WIN_PROBABILITY = .75
NUM_GENERATIONS = 100

# # Functions needed: 

# # fitness(weights)
# # generate_random_weights()
# # generate_initial_population()
# # rank_population()
# # breed(mom, dad)

# def fitness(weights):
#     return naive_accuracy(weights)

# def generate_random_weights():
    

# def generate_initial_population():
#     return

# def rank_population():
#     return

# def breed(mom, dad):
#     return

