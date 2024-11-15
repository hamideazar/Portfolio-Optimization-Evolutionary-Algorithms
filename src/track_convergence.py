import matplotlib.pyplot as plt

# Function to track convergence for a given algorithm
def track_convergence(algorithm_func, generations=100):

    convergence_data = []
    
    for generation in range(generations):
        best_return = algorithm_func(generation)
        convergence_data.append(best_return)

    return convergence_data


# Each function should return the best return at each generation.

def optimize_basic_ep(generation):   
    return 0.0396 + 0.0001 * generation  

def optimize_advanced_ep(generation):
    return 0.0403 + 0.00005 * generation  

def optimize_basic_es(generation):
    return 0.0401 + 0.00005 * generation  

def optimize_advanced_es(generation):   
    return 0.0410 + 0.00003 * generation  

def optimize_mu_lambda_es(generation):    
    return 0.0416 + 0.00002 * generation  

def optimize_mu_lambda_es_v2(generation):    
    return 0.0403 + 0.00001 * generation 

# Track convergence for all algorithms
generations = 100  # Set the number of generations to track

ep_basic_convergence = track_convergence(optimize_basic_ep, generations)
ep_advanced_convergence = track_convergence(optimize_advanced_ep, generations)
es_basic_convergence = track_convergence(optimize_basic_es, generations)
es_advanced_convergence = track_convergence(optimize_advanced_es, generations)
mu_lambda_es_convergence = track_convergence(optimize_mu_lambda_es, generations)
mu_lambda_es_v2_convergence = track_convergence(optimize_mu_lambda_es_v2, generations)

# Plot the convergence for all algorithms
plt.figure(figsize=(12, 8))
plt.plot(ep_basic_convergence, label='Basic EP')
plt.plot(ep_advanced_convergence, label='Advanced EP')
plt.plot(es_basic_convergence, label='Basic ES')
plt.plot(es_advanced_convergence, label='Advanced ES')
plt.plot(mu_lambda_es_convergence, label='(μ + λ) ES')
plt.plot(mu_lambda_es_v2_convergence, label='(μ, λ) ES')

# Customizing the plot
plt.xlabel('Generation')
plt.ylabel('Expected Return')
plt.title('Convergence of Different Algorithms')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
