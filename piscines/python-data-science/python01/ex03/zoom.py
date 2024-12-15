from load_image import ft_load
import cv2


def zoom(img, zoom_factor=20):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor, interpolation=0)


def print_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)


def main():
    img = ft_load("animal.jpeg")
    print_img(img)
    img_zoomed = zoom(img)
    print_img(img_zoomed)
    print(img)


if __name__ == "__main__":
    main()
