## Code Explanation

### 1. Importing Libraries

The following libraries are imported at the beginning of the script:

- **`requests`**: Used to send HTTP requests to fetch earthquake data.
- **`lxml.html`**: Used to parse the HTML content from the fetched data.
- **`datetime`**: For handling date and time conversions.
- **`numpy` (`np`)**: For numerical computations.
- **`matplotlib.pyplot` (`plt`)**: For plotting the data.
- **`hawkeslib`**: For modeling and simulating the Hawkes process.

### 2. Fetching and Parsing Earthquake Data

The script fetches earthquake data from [Kandilli Observatory](http://www.koeri.boun.edu.tr/scripts/lst9.asp) using an HTTP GET request. The data is then parsed to extract relevant earthquake information.

### 3. Extracting Timestamps

The script extracts the timestamps of earthquake events specifically related to Istanbul and converts them to "hours since the first event".

### 4. Plotting the Data

A scatter plot of the earthquake events is generated. The x-axis represents time in hours since the first event.

### 5. Fitting a Hawkes Process

The script fits a Univariate Exponential Hawkes Process (UVHP) to the data and simulates the number of events over a 24-hour period.

### 6. Bayesian Inference with Hawkes Process

The script performs Bayesian inference to estimate the posterior distribution of the Hawkes process parameters, providing insights into the uncertainty of these estimates.
