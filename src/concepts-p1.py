
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
ts = pd.Series(data=np.random.randn(len(dates)), index=dates)

# Use built-in plotting method to visualise the time-series.
fig = ts.plot()


# Perform moving average smoothing.

# Convert the time-series to a dataframe, we'll see the utility of this aftewards.
dates2 = pd.date_range(start="2018-01-01", end="2019-01-01", freq="50H")  
ts2 = pd.Series(data=np.random.randn(len(dates2)), index=dates2)
ts_df  = pd.DataFrame(data=ts2, columns=["Time series"])

# We don't have to index the column as we only have one, for the moment.
ts_df["Moving average"] = ts_df.rolling(5).mean()
ts_df.plot()
