from load_image import ft_load
import cv2


def slice_image(img, window_size, at):
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


def print_img(img):
    """prints an img"""
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("image", img_bgr)
    cv2.waitKey(0)


def main():
    """main function"""
    try:
        img = ft_load("animal.jpeg")
        print(img)
        print_img(img)
        img_zoomed = slice_image(img, 400, [300, 650])
        print(f"New shape after slicing: {img_zoomed.shape}")
        print(img_zoomed)
        print_img(img_zoomed)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
