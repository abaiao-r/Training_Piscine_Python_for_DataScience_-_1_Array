import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape, and returns its pixel data as a numpy
    array.
    Handles JPG and JPEG formats. Prints a clear error message on failure.
    """
    try:
        img = Image.open(path)
        # This checks the file type using the image's format attribute,
        # which is set by PIL.Image.open based on the file's header/magic bytes
        # not just the file extension.
        if img.format not in ("JPEG", "JPG"):
            print(f"Error: Unsupported image format '{img.format}'. "
                  + "Only JPG/JPEG supported.")
            return None
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        return arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
