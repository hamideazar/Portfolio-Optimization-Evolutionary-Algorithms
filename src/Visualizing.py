import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data provided
data = {
    'Algorithm': ['Basic EP', 'Advanced EP', 'Basic ES', 'Advanced ES', '(μ + λ) ES', '(μ, λ) ES'],
    'Final Expected Return': [0.04066, 0.04030, 0.04008, 0.04098, 0.04170, 0.04030],
    'Convergence Speed (Generations)': [5, 5, 5, 5, 5, 5],
    'Stability (Std. Dev.)': [0.002130, 0.001008, 0.001379, 0.001482, 0.000927, 0.001288]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot 1: Final Expected Return
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
plt.bar(df['Algorithm'], df['Final Expected Return'], color='lightblue')
plt.title('Final Expected Return by Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Final Expected Return')
plt.xticks(rotation=45)

# Plot 2: Stability (Std. Dev.)
plt.subplot(1, 2, 2)
plt.bar(df['Algorithm'], df['Stability (Std. Dev.)'], color='lightgreen')
plt.title('Stability (Standard Deviation) by Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Stability (Std. Dev.)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
