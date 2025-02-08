from train.load_csv import load
from estimate_price import estimate_price


class LinearRegression:

    @staticmethod
    def init_data(file: str):
        regression = LinearRegression()
        data = load(file)
        regression.data = data
        regression._normalize_data()

        regression.theta0 = 0
        regression.theta1 = 0
        regression.m = float(len(data))
        return regression

    def train(self, learning_rate: float, iterations: int):
        try:
            for i in range(iterations):
                acc_theta0: float = 0.0
                acc_theta1: float = 0.0
                for row in self.data.itertuples():
                    error = estimate_price(row.km) - row.price
                    acc_theta0 = acc_theta0 + error
                    acc_theta1 = acc_theta1 + error * row.km
                if i % 1000 == 0:
                    print(f"Iter {i}: θ0={self.theta0}, θ1={self.theta1}, Error Prom={acc_theta0/self.m}")
                self.theta0 = self.theta0 - learning_rate * acc_theta0 / self.m
                self.theta1 = self.theta1 - learning_rate * acc_theta1 / self.m
            self._denormalize_theta()

        except BaseException as e:
            print(f"{type(e).__name__}: {e}")

    def _normalize_data(self):
        min_data = min(self.data["km"])
        normalization = max(self.data["km"]) - min_data

        self.data["km"] = (self.data["km"] - min_data) / normalization
        self.min_data = min_data
        self.normalization = normalization

    def _denormalize_theta(self):
        self.theta1 = self.theta1 / self.normalization
        self.theta0 = self.theta0 - self.min_data * self.theta1
