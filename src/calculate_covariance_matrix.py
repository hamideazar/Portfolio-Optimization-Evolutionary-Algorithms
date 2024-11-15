# src/calculate_covariance_matrix.py
import pandas as pd
import os

# Directory paths
results_dir = '../results'

# Load monthly returns data
monthly_returns = pd.read_csv(f"{results_dir}/monthly_returns.csv", index_col=0)

# Calculate covariance matrix
covariance_matrix = monthly_returns.cov()

# Save the covariance matrix to a CSV file
covariance_matrix.to_csv(f"{results_dir}/covariance_matrix.csv")
print("Covariance matrix calculated and saved to covariance_matrix.csv")
