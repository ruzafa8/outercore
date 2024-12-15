import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """This function calculates bmi given an array of weights and heights.
    Returns an array of results.

    Both arrays must have same size, otherwise, error is thrown."""
    h = np.array(height)
    w = np.array(weight)

    assert h.size == w.size, "arrays have not got same size"
    assert (
        np.issubdtype(h.dtype, np.integer)
        or np.issubdtype(h.dtype, np.floating)
    ), "height is not an array of integer or floats"
    assert (
        np.issubdtype(w.dtype, np.integer)
        or np.issubdtype(w.dtype, np.floating)
    ), "weight is not an array of integer or floats"

    return (w / (h**2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function receives a list of int or floats and returns a new list
    with the elements bigger that the limit"""
    h = np.array(bmi)
    assert (
        np.issubdtype(h.dtype, np.integer)
        or np.issubdtype(h.dtype, np.floating)
    ), "height is not an array of integer or floats"
    return (h > limit).tolist()
