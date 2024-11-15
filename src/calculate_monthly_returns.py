import pandas as pd
import os
import glob

# Define directories for data and results
data_dir = '../data'
results_dir = '../results'
os.makedirs(results_dir, exist_ok=True)

# Create an empty DataFrame to collect monthly returns for each stock
monthly_returns = pd.DataFrame()

# Process each CSV file in the data directory
for file_path in glob.glob(f"{data_dir}/*.csv"):
    try:
        # Extract the stock ticker from the file name
        ticker = os.path.splitext(os.path.basename(file_path))[0]

        # Load the CSV and parse the Date column
        df = pd.read_csv(file_path, parse_dates=['Date'])
        
        # Explicitly parse the Date column to ensure format with timezone is handled
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')
        
        # Drop rows with invalid dates
        df.dropna(subset=['Date'], inplace=True)
        df.set_index('Date', inplace=True)

        # Convert 'Adj Close' to numeric, handling any non-numeric data
        df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
        
        # Drop any rows where 'Adj Close' is NaN after conversion
        df.dropna(subset=['Adj Close'], inplace=True)

        # Resample to month-end frequency and calculate monthly returns
        monthly_return_series = df['Adj Close'].resample('ME').ffill().pct_change()

        # If the data for the ticker is valid, add it to the main DataFrame
        if not monthly_return_series.empty:
            monthly_returns[ticker] = monthly_return_series

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Save the collected monthly returns to a CSV if data was processed
if not monthly_returns.empty:
    monthly_returns.dropna().to_csv(f"{results_dir}/monthly_returns.csv")
    print("Monthly returns calculated and saved to monthly_returns.csv")
else:
    print("No valid monthly returns data to save.")
