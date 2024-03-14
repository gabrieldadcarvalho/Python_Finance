""" The function will mnake the comparation
from one wallet with the Brazilian market index (Ibovespa)"""

# Import libary
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Select active wallet
WALLET = {"VALE3.SA": 1000, "PETR4.SA": 1000, "WEGE3.SA": 1000, "IVVB11.SA": 3000, "AAPL34.SA": 2500, "M1TA34.SA": 1500}

# Sum all value invest
SUM_VALUE_INVEST = sum(WALLET.values())

# Getting strat and end date
START_DATE = "2015-01-01"
END_DATE = "2023-08-20"

# Getting stock price on yahoo finance
STOCK_PRICE = yf.download(list(WALLET.keys()), start=START_DATE, end=END_DATE, progress=False)["Adj Close"]
# stock_price = stock_price.set_index(list(WALLET.keys()))
# stock_price = stock_price.dropna()

# Getting price for strat date
PRICE_START_DATE = STOCK_PRICE.iloc[0]

# Transference dic "WALLET" in date frame
WALLET_DF = pd.Series(data=WALLET, index=list(WALLET.keys()), name="STOCK BUY")

# Getting how many stock buy in start day
QUANTITY_STOCK_DAY_ONE = round(WALLET_DF / PRICE_START_DATE - 0.5, 0)

# Variable show equity for day by day
EQUITY = STOCK_PRICE * QUANTITY_STOCK_DAY_ONE

# Creat column "equity" in data frame
EQUITY["Total Equity"] = EQUITY.sum(axis=1)

# Variable show free box in wallet
FREE_BOX = sum(WALLET_DF) - EQUITY["Total Equity"].head(1)

"""COMPARATION OF THE PORTIFOLIO WITH IBOVESPA (^BVSP)"""

# Getting ibovespa data from Yahoo Finance
IBOVESPA = yf.download("^BVSP", start=START_DATE, end=END_DATE, progress=False)["Adj Close"]

# Transformation ibovespa data into a data frame
IBOVESPA = pd.DataFrame(IBOVESPA)

# Modification index data frame ibovespa:
IBOVESPA.rename(columns={"Adj Close": "IBOVESPA"}, inplace=True)

# Joing data frame WALLET with IBOVESPA
WALLET_WITH_INDEX = pd.merge(IBOVESPA, EQUITY, how="inner", on="Date")

# Normalizing data frame WALLET_WITH_INDEX
WALLET_WITH_INDEX = WALLET_WITH_INDEX / WALLET_WITH_INDEX.iloc[0]

# Comparation graphic
plt.plot(WALLET_WITH_INDEX[["IBOVESPA", "Total Equity"]], label=["Ibov", "Wallet"])
plt.xlabel("Date")
plt.ylabel("yield")
plt.legend()
plt.show()
