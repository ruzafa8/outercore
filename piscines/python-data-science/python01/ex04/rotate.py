from load_image import ft_load
import numpy as np
import cv2


def slice_image(img, window_size, at) -> np.array:
    """Given an image, returns a cropped,
    square-shaped copy of size windows_size,
    centered at position at."""
    margin = [
        [
            y + x for y in [-round(window_size/2), round(window_size/2)]
        ] for x in at
    ]
    x_slice = slice(margin[0][0], margin[0][1])
    y_slice = slice(margin[1][0], margin[1][1])
    return img[x_slice, y_slice, :1]


def ft_transpose(img: np.array) -> np.array:
    """Given an numpy array, return the transposed"""
    rows, cols = img.shape
    transposed = np.zeros((cols, rows), dtype=img.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = img[i, j]
    return transposed


def main():
    """main function"""
    try:
        img = ft_load("animal.jpeg")
        cut_image = slice_image(img, 400, [300, 650])
        print(f"The shape of image is: {cut_image.shape}")
        rotated_img = ft_transpose(cut_image[:, :, 0])
        print(cut_image)
        print(f"New shape after Transpose {rotated_img.shape}")
        print(rotated_img)
        cv2.imshow('image', rotated_img)
        cv2.waitKey(0)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
