import numpy as np


def ft_invert(array: np.array) -> np.array:
    return 255 - array


def ft_red(array: np.array) -> np.array:
    array[:, :, ]


def ft_green(array: np.array) -> np.array:
    filtered = array.copy()
    filtered[:, :, 0] = 0
    filtered[:, :, 2] = 0
    return filtered


def ft_blue(array: np.array) -> np.array:
    filtered = array.copy()
    filtered[:, :, 0] = 0
    filtered[:, :, 1] = 0
    return filtered


def ft_grey(array) -> np.array:
    grey_image = array.copy()
    return grey_image[:, :, 0] // 3 + grey_image[:, :, 1] // 3 + grey_image[:, :, 2] // 3
