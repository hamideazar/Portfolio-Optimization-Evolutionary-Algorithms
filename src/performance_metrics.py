import numpy as np

# Final returns for each algorithm from multiple runs 
returns = {
    'Basic EP': [0.0375, 0.0414, 0.0391, 0.0417, 0.0436],  # Results from multiple runs of the algorithm
    'Advanced EP': [0.0390, 0.0414, 0.0412, 0.0407, 0.0392],
    'Basic ES': [0.0389, 0.0392, 0.0388, 0.0420, 0.0415],
    'Advanced ES': [0.0417, 0.0418, 0.0381, 0.0411, 0.0422],
    '(μ + λ) ES': [0.0424, 0.0431, 0.0415, 0.0407, 0.0408],
    '(μ, λ) ES': [0.0403, 0.0396, 0.0389, 0.0427, 0.0400]
}

# Calculate final return, convergence speed, and stability for each algorithm
def calculate_performance_metrics(returns):
    metrics = {}
    for algorithm, values in returns.items():
        final_return = np.mean(values)  # Mean of the final returns
        std_dev = np.std(values)  # Standard deviation for stability
        convergence_speed = len(values)  
        metrics[algorithm] = {
            'Final Expected Return': final_return,
            'Convergence Speed (Generations)': convergence_speed,
            'Stability (Std. Dev.)': std_dev
        }
    return metrics

# Calculate the performance metrics for all algorithms
performance_metrics = calculate_performance_metrics(returns)

# Display the performance metrics in a table format
import pandas as pd
performance_df = pd.DataFrame(performance_metrics).T
print(performance_df)
