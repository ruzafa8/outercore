import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)

    assert arr.ndim == 2, "Array is not 2D"

    print(f"My shape is : {arr.shape}")

    new_array = arr[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
