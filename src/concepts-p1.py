
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Configure the aesthetics
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (25, 15)

# Generate a range of evenly spaced dates, a year with a 10 hour resolution (freq).
dates = pd.date_range(start="2018-01-01", end="2019-01-01", freq="10H")  
# Create a time-series object
ts = pd.Series(
    data=np.random.randn(len(dates)),
    index=dates
)

# Use built-in plotting method to visualise the time-series.
fig = ts.plot()
