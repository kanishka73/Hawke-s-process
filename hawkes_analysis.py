
import pandas as pd
from tick.hawkes import HawkesSumExpKern
from tick.plot import plot_hawkes_kernels, plot_hawkes_kernel_norms

# Load the CSV file
df = pd.read_csv('smaple.csv')

# Extract relevant columns
timestamps = df['timestamp']
retweets = df['retweets']

# Convert timestamps to numerical format (if they are not already)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['timestamp'] = df['timestamp'].astype(int) / 10**9  # convert to seconds since epoch

# Prepare the data for Hawkes process modeling
events = []
for _, row in df.iterrows():
    events.append([row['timestamp']] * int(row['retweets']))

# Flatten the list of lists into a single list
events = [item for sublist in events for item in sublist]

# Fit a Hawkes process model with Sum of Exponential Kernels
decays = [0.1, 1.0, 10.0]  # Example decay parameters
hawkes_sumexp = HawkesSumExpKern(decays=decays, n_threads=1)
hawkes_sumexp.fit([events])

# Plot the estimated kernels
plot_hawkes_kernels(hawkes_sumexp)

# Analyze the intensity function and kernel norms
plot_hawkes_kernel_norms(hawkes_sumexp)
