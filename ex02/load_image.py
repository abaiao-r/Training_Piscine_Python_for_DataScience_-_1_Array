from numpy import array, ndarray
from PIL import Image


def ft_load(path: str) -> 'ndarray':
    """
    Loads an image from the given path, prints its shape, and returns its pixel
    data.
    Args:
        path: Path to the image file.
    Returns:
        NumPy array of image pixels in RGB format.
    Raises:
        Prints a clear error message if loading fails or format is unsupported.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ("JPEG", "JPG"):
                print(f"Error: Unsupported image format '{img.format}'.")
                return None
            img = img.convert("RGB")
            arr = array(img)
            print(f"The shape of image is: {arr.shape}")
            return arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None
