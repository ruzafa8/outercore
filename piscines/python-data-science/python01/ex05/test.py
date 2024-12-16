from load_image import ft_load
from pimp_image import (
  ft_invert,
  ft_red,
  ft_green,
  ft_blue,
  ft_grey
)
import cv2

FUNCTIONS = [
  # ft_invert,
  # ft_red,
  # ft_green,
  # ft_blue,
  ft_grey
]

array = ft_load("landscape.jpg")
for f in FUNCTIONS:
    print(array)
    filtered = f(array)
    print(filtered)
    cv2.imshow("image", filtered)
    cv2.waitKey(0)
