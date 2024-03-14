def DF_IBOVESPA(START_DATE, END_DATE):
    import yfinance as yf
    import pandas as pd

    IBOVESPA = yf.download("^BVSP", start=START_DATE, end=END_DATE, progress=False)["Adj Close"]
    IBOVESPA = pd.DataFrame(IBOVESPA)
    IBOVESPA.rename(columns={"Adj Close": "IBOVESPA"}, inplace=True)
    return IBOVESPA
