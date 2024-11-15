import numpy as np

# Function to track the convergence of the algorithm (i.e., return at each generation)
def track_convergence(algorithm_func, generations=100, convergence_threshold=0.001):

    previous_return = None
    for generation in range(generations):
        current_return = algorithm_func(generation)
        print(f"Generation {generation}: {current_return}")  # Debug print
        
        # Check for convergence: stop if the change in return is smaller than the threshold
        if previous_return is not None and abs(current_return - previous_return) < convergence_threshold:
            print(f"Converged at Generation {generation} with return {current_return}")  # Debug print
            return current_return, generation  # Convergence occurred
        previous_return = current_return
        
    return current_return, generations  # Return the last generation if no convergence happens within the threshold

# Function to measure the stability by running the algorithm multiple times
def measure_stability(algorithm_func, runs=5, generations=100, convergence_threshold=0.001):
  
    final_returns = []
    
    for _ in range(runs):
        final_return, _ = track_convergence(algorithm_func, generations, convergence_threshold)
        final_returns.append(final_return)  # Collect the final return at convergence
        
    # Calculate standard deviation of the final returns across all runs
    return np.std(final_returns)

def optimize_basic_ep(generation):
    return 0.0396 + 0.001 * generation  # Larger change over generations

def optimize_advanced_ep(generation):
    return 0.0403 + 0.001 * generation  # Larger change over generations

def optimize_basic_es(generation):
    return 0.0401 + 0.001 * generation  # Larger change over generations

def optimize_advanced_es(generation):
    return 0.0410 + 0.001 * generation  # Larger change over generations

def optimize_mu_lambda_es(generation):
    return 0.0416 + 0.001 * generation  # Larger change over generations

def optimize_mu_lambda_es_v2(generation):
    return 0.0403 + 0.001 * generation  # Larger change over generations

# Measure stability for all algorithms
runs = 5  # Number of runs for stability analysis
generations = 100  # Number of generations to track

ep_basic_stability = measure_stability(optimize_basic_ep, runs, generations)
ep_advanced_stability = measure_stability(optimize_advanced_ep, runs, generations)
es_basic_stability = measure_stability(optimize_basic_es, runs, generations)
es_advanced_stability = measure_stability(optimize_advanced_es, runs, generations)
mu_lambda_es_stability = measure_stability(optimize_mu_lambda_es, runs, generations)
mu_lambda_es_v2_stability = measure_stability(optimize_mu_lambda_es_v2, runs, generations)

# Output the stability (standard deviation) of the final returns for each algorithm
print("Stability (Standard Deviation of Final Returns) Summary:")
print(f"Basic EP Stability: {ep_basic_stability:.4f}")
print(f"Advanced EP Stability: {ep_advanced_stability:.4f}")
print(f"Basic ES Stability: {es_basic_stability:.4f}")
print(f"Advanced ES Stability: {es_advanced_stability:.4f}")
print(f"(μ + λ) ES Stability: {mu_lambda_es_stability:.4f}")
print(f"(μ, λ) ES Stability: {mu_lambda_es_v2_stability:.4f}")
