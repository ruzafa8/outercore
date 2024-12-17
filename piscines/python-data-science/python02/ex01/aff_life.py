import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        data = load("life_expectancy_years.csv")
        assert data is not None, "Error with data"

        years = data.columns[1:]
        row = data[data["country"] == "Spain"]
        life_expectancy = row.values[0][1:]

        plt.plot(years, life_expectancy)
        plt.title('Spain Life Expectancy Projections')
        plt.xlabel('Year')
        plt.xticks(years[::40])
        plt.ylabel('Life Expectancy')
        plt.yticks(range(30, 101, 10))
        plt.show()

    except BaseException as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
