"""
This module contains the logic for solving the tsp through
a genetic algorithm.
"""

from multiprocessing import Pool
from functools import partial
import numpy as np
import random

Number = float | int

def generate_initial_population(dist_matrix, no_of_individuals: int = 50):
    individuals = []
    chromosome_length = len(dist_matrix)
    
    for _ in range(no_of_individuals):
        individual = np.arange(1, chromosome_length)
        np.random.shuffle(individual)
        individuals.append(individual)
        
    return np.array(individuals).tolist()

def fitness(chromozome: np.array, dist_matrix: np.array):
    cost:Number = 0
    for node, next_node in zip(chromozome[1:], chromozome[:-1]):
        cost += dist_matrix[node][next_node]
    cost += dist_matrix[chromozome[-1]][chromozome[0]]
    return cost

def tournament_selection(population, fitnesses, tournament_size=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
        tournament_winner = min(tournament, key=lambda ind: ind[1])
        selected.append(tournament_winner)
    return selected

def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    
    child1 = [None] * size
    child2 = [None] * size
    
    child1[start:end+1] = parent1[start:end+1]
    child2[start:end+1] = parent2[start:end+1]
    
    def fill_child(child, parent):
        current_pos = (end + 1) % size
        for gene in parent:
            if gene not in child:
                while child[current_pos] is not None:
                    current_pos = (current_pos + 1) % size
                child[current_pos] = gene
        return child
    
    return fill_child(child1, parent2), fill_child(child2, parent1)

def swap_mutation(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def genetic_algorithm(dist_matrix,
                      no_of_individuals:int=50,
                      no_of_generations:int=100,
                      tournament_size:int=3,
                      mutation_rate:float=0.1,
                      no_of_processes:int=4):
    population = generate_initial_population(dist_matrix, no_of_individuals)
    best_solution = None
    best_fitness = float('inf')
    
    partial_fitness = partial(fitness, dist_matrix=dist_matrix)
    partial_tournament = partial(tournament_selection, tournament_size=tournament_size)
    
    for _ in range(no_of_generations):
        with Pool(no_of_processes) as p:
            fitnesses = p.map(partial_fitness, population)
        
        for ind, fit in zip(population, fitnesses):
            if fit < best_fitness:
                best_solution = ind
                best_fitness = fit
        
        print(list(zip(population, fitnesses)))
        with Pool(no_of_processes) as p:
            selected_parents = p.starmap(partial_tournament, zip(population, fitnesses))
        
        offspring = []
        for i in range(0, len(selected_parents), 2):
            if i + 1 < len(selected_parents):
                child1, child2 = order_crossover(selected_parents[i][0], selected_parents[i + 1][0])
                offspring.extend([child1, child2])
            else:
                offspring.append(selected_parents[i][0])
        
        population = [swap_mutation(ind, mutation_rate) for ind in offspring]
        
    return best_solution, best_fitness