import argparse
from linear_regression.train import LinearRegression


def main():
    parser = argparse.ArgumentParser(description="Linear regression project.")
    parser.add_argument("file", help='file name of the csv data', nargs="?",
                        default='theta.data')
    args = parser.parse_args()

    try:
        theta0, theta1 = read_theta_file(args.file)
        print(theta0, theta1)
        regression = LinearRegression.load_theta(theta0, theta1)
        while True:
            mileage = int(input("Insert a mileage to predict price: "))
            print(regression.estimate_price(mileage))
    except ValueError:
        pass
    except AssertionError as e:
        print(e)
    except BaseException as e:
        print(f"{type(e).__name__}: {e}")


def read_theta_file(file: str):
    try:
        with open(file, "r") as file:
            line = file.readline()
            assert line is not None, "file empty"
            assert line.count(":") == 1, "incorrect file format"
            tokens = line.split(":")
            return float(tokens[0]), float(tokens[1])
    except ValueError:
        raise AssertionError("incorrect file format")
    except FileNotFoundError:
        raise AssertionError("file not found")


if __name__ == "__main__":
    main()
