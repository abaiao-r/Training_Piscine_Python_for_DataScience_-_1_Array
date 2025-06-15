from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """
    Loads an image from the given path, prints its shape and pixel data in RGB format,
    and returns it as a NumPy array.

    Args:
        path (str): Path to the image file.

    Returns:
        array: NumPy array of image pixels in RGB format.
               Returns an empty array if loading fails or format unsupported.

    Prints clear error messages if loading fails or format is unsupported.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ("JPEG", "JPG"):
                print(f"Error: Unsupported image format '{img.format}'.")
                return array([])
            img = img.convert("RGB")
            arr = array(img)
            print(f"The shape of image is: {arr.shape}")
            print(arr)
            return arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return array([])
