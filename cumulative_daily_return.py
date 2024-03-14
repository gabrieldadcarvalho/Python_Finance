import numpy as np
import pandas as pd
import plotly.express as px
import yfinance as yf

# Select active wallet
WALLET = ['LWSA3.SA', 'PETR4.SA', 'BBAS3.SA', 'IVVB11.SA', 'CSRN3.SA', 'ZAMP3.SA', 'NTCO3.SA', 'COCA34.SA']

# Getting strat and end date
START_DATE = "2018-01-01"
END_DATE = "2023-12-07"

# The weight of a investiment portfolio
WEIGHT = np.array([0.2, 0.1, 0.1, 0.2, 0.05, 0.05, 0.2, 0.1])

# Portifolio Data Frame
DF_WALLET = yf.download(WALLET, start=START_DATE, end=END_DATE, progress=False)["Adj Close"]

# IBOVESPA Data Frame
IBOV = yf.download("^BVSP", start=START_DATE, end=END_DATE, progress=False)["Adj Close"]

# Return of each active in the wallet
"""
.pct_change() vai comparar a variação
com a proxima linha do data frame.
"""
RETURN = DF_WALLET.pct_change()
RETURN = RETURN.dropna()

# Daily return of each in the wallet
"""
Axies=0 -> Line
Axies=1 -> Column
"""
RETURN_WEIGHTED = RETURN * WEIGHT
RETURN_DAILY_WALLET = RETURN_WEIGHTED.sum(axis=1)

# Acumulative return of each in the wallet
RETURN_ACUMULATIVE_WALLET = (RETURN_DAILY_WALLET + 1).cumprod() - 1

# Daily return of each in the IBOVESPA
RETURN_IBOV = IBOV.pct_change()

# Acumulative return of each in the IBOVESPA
RETURN_ACUMULATIVE_IBOV = (RETURN_IBOV + 1).cumprod() - 1

# Creating data frame with the return WALLET and IBOVESPA
DF_RETURN_ACUMULATIVE_IBOV_WALLET = pd.DataFrame()
DF_RETURN_ACUMULATIVE_IBOV_WALLET["WALLET"] = RETURN_ACUMULATIVE_WALLET
DF_RETURN_ACUMULATIVE_IBOV_WALLET["IBOV"] = RETURN_ACUMULATIVE_IBOV
"""
.dropnan() -> removendo dados faltantes 'Nan'.
"""
DF_RETURN_ACUMULATIVE_IBOV_WALLET = DF_RETURN_ACUMULATIVE_IBOV_WALLET.dropna()

# Ploting graph
fig = px.line(DF_RETURN_ACUMULATIVE_IBOV_WALLET)
fig.show()
