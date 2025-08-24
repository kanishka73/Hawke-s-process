
# Import necessary libraries
import requests
from lxml import html
from datetime import datetime as dt
import numpy as np
from matplotlib import pyplot as plt

# Fetch data from a URL that lists recent earthquake events
res = requests.get("http://www.koeri.boun.edu.tr/scripts/lst9.asp")

# Parse the content of the page and extract the relevant text
tx = html.fromstring(res.content).xpath("//pre/text()")[0]

# Split the text into lines and skip the first 7 lines (headers)
lines = tx.splitlines()[7:]

# Extract timestamps for events in ISTANBUL and convert them to datetime objects
timestamps = [dt.strptime(l[:19], "%Y.%m.%d %H:%M:%S") for l in lines if "ISTANBUL" in l]

# Calculate the time difference in hours since the first event
t = np.array([(x - timestamps[-1]).total_seconds() / 3600 for x in timestamps])[::-1]

# Plot the timestamps with random y-values for a scatter plot
plt.figure(figsize=(15, 2))
plt.ylim([-5, 5])  # Set y-axis limits
plt.yticks([])  # Hide y-axis ticks
_ = plt.plot(t, np.random.rand(len(t)), 'k.')  # Plot with black dots

# Measure the time taken for the following block of code to execute
#%%time

# Import UnivariateExponential Hawkes Process from hawkeslib
from hawkeslib import UnivariateExpHawkesProcess as UVHP

# Initialize the Hawkes process model
uv = UVHP()

# Fit the model to the time data
uv.fit(t)

# Print the model parameters
print(uv.get_params())

# Simulate the process and collect the number of events (shocks) in 24-hour intervals
nr_shocks_sample = [len(uv.sample(24)) for x in range(100000)]

# Plot a histogram of the number of shocks over the simulations
_ = plt.hist(nr_shocks_sample, bins=20)

# Import Bayesian Univariate Exponential Hawkes Process from hawkeslib
from hawkeslib import BayesianUVExpHawkesProcess as BUVHP

# Initialize the Bayesian Hawkes process model with extended hyperparameters
buv = BUVHP(
    mu_hyp=(1., 10.),          # Prior for the background intensity (mu)
    alpha_hyp=(1., 1.),        # Prior for the excitation parameter (alpha)
    theta_hyp=(1., 10.),       # Prior for the decay rate (theta)
    mu_beta_hyp=(2., 0.5),     # Additional prior for mu with beta distribution
    alpha_beta_hyp=(2., 2.),   # Additional prior for alpha with beta distribution
    theta_gamma_hyp=(2., 1.)   # Additional prior for theta with gamma distribution
)

# Sample the posterior distribution using the observed time data
trace = buv.sample_posterior(t, T=t[-1], n_samp=50000)

# Compute and print the Bayesian credible intervals (BCIs) for 'mu', 'alpha', and 'theta'
print(pm.stats.quantiles(trace["mu"], [2.5, 97.5]))
print(pm.stats.quantiles(trace["alpha"], [2.5, 97.5]))
print(pm.stats.quantiles(trace["theta"], [2.5, 97.5]))
