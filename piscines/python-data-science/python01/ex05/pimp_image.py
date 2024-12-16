import numpy as np


def ft_invert(array: np.array) -> np.array:
    """Given an image, return a newone with the colours
    inverted"""
    return 255 - array


def ft_red(array: np.array) -> np.array:
    """Given an image, return a newone with a red mask"""
    return (array * [0, 0, 1]).astype(np.uint8)


def ft_green(array: np.array) -> np.array:
    """Given an image, return a newone with a green mask"""
    filtered = array.copy()
    filtered[:, :, 0] -= filtered[:, :, 0]
    filtered[:, :, 2] -= filtered[:, :, 2]
    return (array * [0, 1, 0]).astype(np.uint8)


def ft_blue(array: np.array) -> np.array:
    """Given an image, return a newone with a blue mask"""
    filtered = array.copy()
    filtered[:, :, 1] = 0
    filtered[:, :, 2] = 0
    return filtered.astype(np.uint8)


def ft_grey(array) -> np.array:
    """Given an image, return a newone in a grayscale"""
    return (np.sum(array, axis=2) / 3).astype(np.uint8)
