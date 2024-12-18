import matplotlib.pyplot as plt
from load_csv import load


def main():
    income_csv = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_csv = load("life_expectancy_years.csv")

    # breakpoint()

    x = income_csv["1900"]
    y = life_csv["1900"]

    plt.title('1900')
    plt.plot(x, y, 'o')

    plt.xlabel('Gross domestic product')
    plt.xscale('log')
    plt.xticks(
        [300, 1_000, 10_000],
        ["300", "1k", "10k"]
    )

    plt.ylabel('Life Expectancy')
    plt.show()


if __name__ == "__main__":
    main()
