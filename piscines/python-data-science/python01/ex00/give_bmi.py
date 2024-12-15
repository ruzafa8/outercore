import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    h = np.array(height)
    w = np.array(weight)

    return (w / (h**2)).tolist()


def apply_limit(height: list[int | float], limit: int) -> list[bool]:
    return ((lambda x: x > limit)(np.array(height))).tolist()
