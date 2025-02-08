from theta import Theta


def estimate_price(mileage: int) -> int:
    return Theta.get_theta0() + Theta.get_theta1() * mileage
