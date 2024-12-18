import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def parse_number(number: str) -> float:
    """This function parses a number from str
    to float. The number can finish in M or K,
    where M means million and K thousands."""
    if number.endswith("M"):
        return float(number[:-1]) * 1_000_000
    if number.endswith("K"):
        return float(number[:-1]) * 1_000
    return float(number)


def from_country(csv: pd.DataFrame, country: str) -> pd.DataFrame:
    """This function selects the data of an specific country
    in the dataset"""
    return csv[csv["country"] == country].values[0][1:]


def main():
    """This function reads a population CSV file
    and plots the data of Spain and France"""
    try:
        csv = load("population_total.csv")
        assert csv is not None, "Error with data"

        parser = np.vectorize(parse_number)

        years = csv.columns[1:].astype(int)
        spain_row = parser(from_country(csv, "Spain"))
        france_row = parser(from_country(csv, "France"))

        plt.title('Population Projections')

        plt.plot(years, spain_row, label="Spain", color="blue")
        plt.plot(years, france_row, label="France", color="green")

        plt.xlabel('Year')
        plt.xticks(range(1800, 2051, 40))
        plt.xlim(1800, 2050)

        plt.ylabel('Population')
        y_ticks = np.linspace(0, max(max(spain_row), max(france_row)), 5)
        plt.yticks(
            y_ticks,
            ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks]
        )
        plt.legend(loc="lower right")

        plt.tight_layout()
        plt.show()

    except BaseException as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
