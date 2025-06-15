import numpy
import matplotlib.pyplot

from load_image import ft_load


def zoom_image(image: numpy.ndarray, top: int, left: int,
               height: int, width: int) -> numpy.ndarray:
    """
    Return a zoomed (sliced) version of the image with one color channel.

    Args:
        image (numpy.ndarray): Original image array.
        top (int): Y-axis starting index.
        left (int): X-axis starting index.
        height (int): Height of the zoom area.
        width (int): Width of the zoom area.

    Returns:
        numpy.ndarray: Sliced image of shape (height, width, 1).
    """
    if image is None:
        raise ValueError("Error: Input image is None")
    zoomed = image[top:top + height, left:left + width, 0:1]
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)
    return zoomed


def display_image(image: numpy.ndarray, image_title: str) -> None:
    """
    Display an image with labeled axes using matplotlib.

    Args:
        image (numpy.ndarray): 2D or 3D image array.
        image_title (str): Title of the displayed image.
    """
    matplotlib.pyplot.imshow(image.squeeze(), cmap="gray")
    matplotlib.pyplot.title(image_title)
    matplotlib.pyplot.xlabel("X axis (pixels)")
    matplotlib.pyplot.ylabel("Y axis (pixels)")
    matplotlib.pyplot.colorbar(label="Pixel intensity")
    matplotlib.pyplot.grid(False)
    matplotlib.pyplot.show()


def main():
    """
    Main function to load an image, zoom, and display it.
    """
    image = ft_load("../animal.jpeg")
    if image is None:
        return

    print(image)

    zoomed = zoom_image(image, 100, 300, 400, 400)

    display_image(zoomed, "Zoomed Image (1 channel)")


if __name__ == "__main__":
    main()
