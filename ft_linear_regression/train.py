import argparse
from linear_regression.train import LinearRegression


def linear_regression_train():
    try:
        args = parse_params()

        regression = LinearRegression.load_file(args.file)
        regression.train(learning_rate=args.learning_rate,
                         iterations=args.iterations, debug=args.debug)

        print("============================================")
        print("Training result:")
        print("θ₀ = ", regression.theta0)
        print("θ₁ = ", regression.theta1)
        print("============================================")
        if args.accuracy:
            print("Accuracy measurement:")
            print(regression.get_accuracy())
            print("============================================")

        if args.plot:
            regression.plot_data()

        with open(args.output, "w") as file:
            file.write(f"{regression.theta0}:{regression.theta1}")
    except AssertionError as e:
        print(e)
    except BaseException as e:
        print(f"{type(e).__name__}: {e}")


def parse_params():
    parser = argparse.ArgumentParser(description="Linear regression project.")
    parser.add_argument("file", help='file name of the csv data', nargs="?",
                        default='data.csv')
    parser.add_argument("-l", "--learning-rate", type=float, default=0.01)
    parser.add_argument("-i", "--iterations", type=int, default=10000)
    parser.add_argument("-o", "--output", type=str, default="theta.data")
    parser.add_argument("-p", "--plot", action="store_true", default=False,
                        help="plot result of training in a graphic.")
    parser.add_argument("-d", "--debug", action="store_true", default=False,
                        help="show debug training info.")
    parser.add_argument("-a", "--accuracy", action="store_true", default=False,
                        help="show model accuracy.")
    return parser.parse_args()


if __name__ == '__main__':
    linear_regression_train()
