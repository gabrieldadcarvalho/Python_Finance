def DF_SELIC_RATE(START_DATE, END_DATE):
    from bcb import sgs

    SELIC_RATE = sgs.get(("selic", 432), start=START_DATE, end=END_DATE)
    SELIC_RATE.rename(columns={"selic": "SELIC_RATE"}, inplace=True)
    return SELIC_RATE
