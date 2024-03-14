import yfinance as yf
import plotly.express as px
import numpy as np

# Select active wallet
WALLET = ["BPAC11.SA"]

# Getting strat and end date
START_DATE = "2018-01-01"
END_DATE = "2021-05-30"

# The weight of a investiment portfolio
WEIGHT = np.array([1])

# Portifolio Data Frame
DF_WALLET = yf.download(WALLET, start=START_DATE, end=END_DATE, progress=False)["Adj Close"]

# Compare the variance with the next line of the data frame
RETURN = DF_WALLET.pct_change()

# Getting return of week. resample('W') -> 'W' = 'Week; 'Y' = 'Year'
RETURN_MEAN_YEAR = (RETURN * WEIGHT).resample("Y").mean()

# Description of portfolio statistics
STATISTICS_WALLET = RETURN.describe()

MEAN_MOVING_RETURN = RETURN.rolling(window=15).mean()
print(MEAN_MOVING_RETURN)

# Plotting graph year
FIG_YEAR = px.line(MEAN_MOVING_RETURN)
FIG_YEAR.update_layout(title="Return Mean Year", xaxis_title="Date", yaxis_title="Return")
FIG_YEAR.update_traces(name=WALLET[0])
FIG_YEAR.show()
