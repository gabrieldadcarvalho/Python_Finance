def COMPARATION_SELIC_IBOV(START_DATE, END_DATE):
    # Import libary
    from bcb import sgs
    import yfinance as yf
    import pandas as pd
    import matplotlib.pyplot as plt

    # Getting strat and end date
    """
    START_DATE = '2010-01-01'
    END_DATE = '2023-09-09'
    """
    # Select selic tax
    SELIC_RATE = sgs.get(("selic", 432), start=START_DATE, end=END_DATE)
    # SELIC_RATE.index.name = "Data"

    # Getting ibovespa data from Yahoo Finance
    IBOVESPA = yf.download("^BVSP", start=START_DATE, end=END_DATE, progress=False)["Adj Close"]

    # Transformation ibovespa data into a data frame
    IBOVESPA = pd.DataFrame(IBOVESPA)

    # Modification index data frame ibovespa:
    IBOVESPA.rename(columns={"Adj Close": "IBOVESPA"}, inplace=True)
    """
    IBOVESPA.index.name = "Data"
    """

    # Append IBOVESPA and SELIC_RATE in unique Data Frame
    COMPARISON = pd.merge(IBOVESPA, SELIC_RATE, how="inner", on="Date")  # type: ignore

    # Criar uma figura e um eixo
    fig, ax1 = plt.subplots()

    # Plotar o primeiro conjunto de dados no eixo principal
    ax1.plot(COMPARISON.index, COMPARISON["IBOVESPA"], label="IBOVESPA")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("IBOVESPA", color="b")

    # Criar um segundo eixo y que compartilha o mesmo eixo x
    ax2 = ax1.twinx()

    # Plotar o segundo conjunto de dados no segundo eixo y
    ax2.plot(COMPARISON.index, COMPARISON["selic"], color="r", label="Taxa Selic")
    ax2.set_ylabel("Taxa Selic", color="r")

    # Adicionar legendas
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc="upper left", bbox_to_anchor=(1, 1))

    # Plot graph
    return plt.show()


START_DATE = "2018-01-01"
END_DATE = "2023-08-20"
COMPARATION_SELIC_IBOV(START_DATE, END_DATE)
