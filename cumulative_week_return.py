import yfinance as yf
import numpy as np
import plotly.express as px

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
RETURN_MEAN_WEEK = (RETURN * WEIGHT).resample("W").mean()

# Ploting graph week
FIG_WEEK = px.line(RETURN_MEAN_WEEK)
FIG_WEEK.update_layout(title="Return Mean Week", xaxis_title="Date", yaxis_title="Return")
FIG_WEEK.update_traces(name="BTG_PACTUAL")
FIG_WEEK.show()

# Ploting histogram graph
FIG_HIST = px.histogram(RETURN, nbins=50)
FIG_HIST.show()
