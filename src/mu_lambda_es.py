import numpy as np
import pandas as pd
import random

# Load the monthly returns data from CSV
monthly_returns = pd.read_csv('../results/monthly_returns.csv', index_col=0)

# Calculate expected returns as the mean of monthly returns for each stock
expected_returns = monthly_returns.mean()

# Parameters
mu = 50            # Population size (μ)
lambd = 100        # Offspring size (λ)
generations = 100
initial_mutation_rate = 0.1

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

# (μ, λ) Evolutionary Strategy
def mu_comma_lambda_es(returns, generations, mu, lambd, mutation_rate):
    population = initialize_population(mu, len(returns))
    for _ in range(generations):
        # Generate offspring population by mutating the parent population
        offspring = [mutate(random.choice(population), mutation_rate) for _ in range(lambd)]
        
        # Sort offspring by fitness and select the top μ individuals for the next generation
        offspring.sort(key=lambda w: fitness(w, returns), reverse=True)
        population = offspring[:mu]
    
    # Return the best portfolio from the final population
    return max(population, key=lambda w: fitness(w, returns))

# Run (μ, λ) ES
best_portfolio_mu_comma_lambda = mu_comma_lambda_es(expected_returns, generations, mu, lambd, initial_mutation_rate)
print("Best Portfolio Weights (μ, λ ES):", best_portfolio_mu_comma_lambda)
print("Expected Return (μ, λ ES):", fitness(best_portfolio_mu_comma_lambda, expected_returns))
