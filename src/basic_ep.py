import numpy as np
import pandas as pd

# Load data
monthly_returns = pd.read_csv('../results/monthly_returns.csv', index_col=0)
expected_returns = monthly_returns.mean()

# Parameters
population_size = 50
generations = 100
mutation_rate = 0.1

# Initialize random portfolios
def initialize_population(size, num_assets):
    return [np.random.dirichlet(np.ones(num_assets), size=1)[0] for _ in range(size)]

# Fitness function: Expected return of the portfolio
def fitness(weights, returns):
    return np.dot(weights, returns)

# Mutation function
def mutate(weights, rate):
    mutated_weights = weights + rate * np.random.randn(len(weights))
    mutated_weights = np.clip(mutated_weights, 0, 1)
    return mutated_weights / np.sum(mutated_weights)

# Evolutionary Programming Algorithm
def basic_ep(returns, generations, population_size, mutation_rate):
    population = initialize_population(population_size, len(returns))
    for _ in range(generations):
        # Mutate individuals
        offspring = [mutate(individual, mutation_rate) for individual in population]
        
        # Combine population and offspring
        combined_population = population + offspring
        # Sort based on fitness and select top population_size individuals
        combined_population.sort(key=lambda w: fitness(w, returns), reverse=True)
        population = combined_population[:population_size]
    
    # Return the best portfolio
    return max(population, key=lambda w: fitness(w, returns))

# Run Basic EP
best_portfolio_ep = basic_ep(expected_returns, generations, population_size, mutation_rate)
print("Best Portfolio Weights (EP):", best_portfolio_ep)
print("Expected Return (EP):", fitness(best_portfolio_ep, expected_returns))
