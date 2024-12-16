import numpy as np
import cv2


def ft_load(path: str) -> np.array:
    assert (
        path.endswith("jpg")
        or path.endswith("jpeg")
    ), "format not supported"
    img = cv2.imread(path)

    assert img is not None, "invalid file path"
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return rgb_img