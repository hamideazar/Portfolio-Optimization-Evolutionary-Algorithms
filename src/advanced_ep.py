import numpy as np
import pandas as pd
import random

# Load data
monthly_returns = pd.read_csv('../results/monthly_returns.csv', index_col=0)
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

# Advanced EP with self-adaptive mutation
def advanced_ep(returns, generations, population_size, mutation_rate):
    population = initialize_population(population_size, len(returns))
    for generation in range(generations):
        # Generate offspring with adaptive mutation
        offspring = [adaptive_mutate(individual, mutation_rate, generation) for individual in population]
        
        # Combine population and offspring
        combined_population = population + offspring
        combined_population.sort(key=lambda w: fitness(w, returns), reverse=True)
        
        # Select top-performing individuals
        population = combined_population[:population_size]
    
    return max(population, key=lambda w: fitness(w, returns))

# Run Advanced EP
best_portfolio_adv_ep = advanced_ep(expected_returns, generations, population_size, initial_mutation_rate)
print("Best Portfolio Weights (Advanced EP):", best_portfolio_adv_ep)
print("Expected Return (Advanced EP):", fitness(best_portfolio_adv_ep, expected_returns))
