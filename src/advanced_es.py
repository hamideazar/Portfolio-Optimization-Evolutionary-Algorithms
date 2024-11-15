import numpy as np
import pandas as pd
import random

# Load the monthly returns data from CSV
monthly_returns = pd.read_csv('../results/monthly_returns.csv', index_col=0)

# Calculate expected returns as the mean of monthly returns for each stock
expected_returns = monthly_returns.mean()

# Parameters
population_size = 50
generations = 100
initial_mutation_rate = 0.1

# Initialize random portfolios
def initialize_population(size, num_assets):
    return [np.random.dirichlet(np.ones(num_assets), size=1)[0] for _ in range(size)]

# Fitness function: Expected return of the portfolio
def fitness(weights, returns):
    return np.dot(weights, returns)

# Mutation function with self-adaptive mutation rate
def adaptive_mutate(weights, initial_rate, generation):
    rate = initial_rate / (1 + generation * 0.01)  # Reduce mutation rate over time
    mutated_weights = weights + rate * np.random.randn(len(weights))
    mutated_weights = np.clip(mutated_weights, 0, 1)
    return mutated_weights / np.sum(mutated_weights)

# Recombination (simple average of two parents)
def recombine(parent1, parent2):
    child = (parent1 + parent2) / 2
    return child / np.sum(child)  # Ensure weights sum to 1

# Advanced ES with self-adaptive mutation
def advanced_es(returns, generations, population_size, mutation_rate):
    population = initialize_population(population_size, len(returns))
    for generation in range(generations):
        offspring = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(population, 2)  # Select two parents
            child = recombine(parent1, parent2)
            mutated_child = adaptive_mutate(child, mutation_rate, generation)
            offspring.append(mutated_child)
        
        # Select top-performing individuals
        combined_population = population + offspring
        combined_population.sort(key=lambda w: fitness(w, returns), reverse=True)
        population = combined_population[:population_size]
    
    return max(population, key=lambda w: fitness(w, returns))

# Run Advanced ES
best_portfolio_adv_es = advanced_es(expected_returns, generations, population_size, initial_mutation_rate)
print("Best Portfolio Weights (Advanced ES):", best_portfolio_adv_es)
print("Expected Return (Advanced ES):", fitness(best_portfolio_adv_es, expected_returns))
