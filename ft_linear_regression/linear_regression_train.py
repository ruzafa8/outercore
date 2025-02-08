import argparse
from train.train import LinearRegression


def linear_regression_train():
    parser = argparse.ArgumentParser(description="Linear regression project.")
    parser.add_argument("file", help='file name of the csv data', nargs="?", default='data.csv')
    parser.add_argument("-l", "--learning-rate", type=float, default=0.01)
    parser.add_argument("-i", "--iterations", type=int, default=10000)
    parser.add_argument("-o", "--output", type=str, default="theta.data")
    args = parser.parse_args()

    regression = LinearRegression.init_data(args.file)
    regression.train(learning_rate=args.learning_rate, iterations=args.iterations)

    print("Theta0: ", Theta.get_theta0())
    print("Theta1: ", Theta.get_theta1())
    with open(args.output, "w") as file:
        file.write(f"{Theta.get_theta0()}:{Theta.get_theta1()}")


if __name__ == '__main__':
    linear_regression_train()
