def DF_TICKET(NAME, START_DATE, END_DATE):
    import yfinance as yf
    import pandas as pd

    TICKET = yf.download(f"{NAME}", start=START_DATE, end=END_DATE, progress=False)["Adj Close"]
    TICKET = pd.DataFrame(TICKET)
    TICKET.rename(columns={"Adj Close": f"{NAME}"}, inplace=True)
    return TICKET
