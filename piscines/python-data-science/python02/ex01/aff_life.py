# import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load("life_expectancy_years.csv")
    print(data)
    # data.plot(x="", title="Test")
    # plt.show()


if __name__ == "__main__":
    main()
