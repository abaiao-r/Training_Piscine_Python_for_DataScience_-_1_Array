from PIL import Image
from numpy import array, ndarray


def ft_load(path: str) -> 'ndarray':
    """
    Loads an image, crops a square from the center, and converts it to grayscale.
    Args:
        path: Path to the image file.
    Returns:
        NumPy array of the cropped grayscale image.
    """
    try:
        with Image.open(path) as img:
            img = img.convert("L")
            width, height = img.size
            side = min(width, height, 400)
            left = (width - side) // 2
            top = (height - side) // 2
            right = left + side
            bottom = top + side
            img_cropped = img.crop((left, top, right, bottom))
            arr = array(img_cropped)
            arr = arr.reshape((side, side, 1))
            print(f"The shape of image is: {arr.shape}")
            print(arr)
            return arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None
