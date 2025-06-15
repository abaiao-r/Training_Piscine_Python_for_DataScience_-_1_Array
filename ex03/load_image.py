import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path if it is in JPG or JPEG format.

    Parameters:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image as a NumPy array, or None if an error occurs.
    """
    try:
        img = Image.open(path)

        # Check if image format is JPEG or JPG
        if img.format not in ("JPEG", "JPG"):
            print(f"Error: Unsupported image format '{img.format}'. "
                  + "Only JPG/JPEG supported.")
            return None

        # Convert image to numpy array
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
