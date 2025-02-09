from linear_regression.load_csv import load
import matplotlib.pyplot as plt


class LinearRegression:
    def estimate_price(self, mileage: int) -> int:
        return self.theta0 + self.theta1 * mileage

    @staticmethod
    def load_file(file: str):
        regression = LinearRegression()
        data = load(file)
        regression.data = data
        regression.original_data = data.copy()
        regression._normalize_data()

        regression.theta0 = 0
        regression.theta1 = 0
        regression.m = float(len(data))
        return regression

    @staticmethod
    def load_theta(theta0, theta1):
        regression = LinearRegression()
        regression.theta0 = theta0
        regression.theta1 = theta1
        return regression

    def train(self, learning_rate: float, iterations: int, debug: bool):
        try:
            for i in range(iterations):
                acc_theta0: float = 0.0
                acc_theta1: float = 0.0
                for row in self.data.itertuples():
                    error = self.estimate_price(row.km) - row.price
                    acc_theta0 = acc_theta0 + error
                    acc_theta1 = acc_theta1 + error * row.km
                if debug and i % 1000 == 0:
                    pass
                    print(f"Iter {i}: θ0={self.theta0}, θ1={self.theta1},\
                          Error Prom={acc_theta0/self.m}")
                self.theta0 = self.theta0 - learning_rate * acc_theta0 / self.m
                self.theta1 = self.theta1 - learning_rate * acc_theta1 / self.m
            self._denormalize_theta()

        except BaseException as e:
            print(f"{type(e).__name__}: {e}")

    def plot_data(self):
        data = self.original_data

        plt.plot(data.km, data.price, 'o')
        plt.axline((0, self.theta0), slope=self.theta1, color='g')

        plt.title('kms/price')
        plt.xlabel('kms')
        plt.ylabel('price')

        plt.show()

    def get_accuracy(self):
        pred = [self.estimate_price(km) for km in self.original_data.km]
        RSS = sum((self.original_data.price - pred) ** 2)
        TSS = sum((
            self.original_data.price - self.original_data.price.mean()) ** 2)
        R2 = 1 - RSS / TSS

        MAE = sum(abs(self.original_data.price - pred)) / self.m
        RMSE = (RSS / self.m) ** 0.5
        return {
            "R2": R2,      # (0, 1)
            "MAE": MAE,    # mean of errors
            "RMSE": RMSE,  # espected difference between prediction and real
        }

    def _normalize_data(self):
        min_data = min(self.data["km"])
        normalization = max(self.data["km"]) - min_data

        self.data["km"] = (self.data["km"] - min_data) / normalization
        self.min_data = min_data
        self.normalization = normalization

    def _denormalize_theta(self):
        self.theta1 = self.theta1 / self.normalization
        self.theta0 = self.theta0 - self.min_data * self.theta1
