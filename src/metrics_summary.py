import pandas as pd

# Performance Metrics Summary
metrics_summary = {
    'Algorithm': ['Basic EP', 'Advanced EP', 'Basic ES', 'Advanced ES', '(μ + λ) ES', '(μ, λ) ES'],
    'Final Expected Return': [0.04066, 0.04030, 0.04008, 0.04098, 0.04170, 0.04030],
    'Convergence Speed (Generations)': [5.0, 5.0, 5.0, 5.0, 5.0, 5.0],  # all values for convergence speed
    'Stability (Std. Dev.)': [0.002130, 0.001008, 0.001379, 0.001482, 0.000927, 0.001288]  # values for stability
}

df_summary = pd.DataFrame(metrics_summary)
print(df_summary)
