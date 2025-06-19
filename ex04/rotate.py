import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def crop_and_gray(img: np.ndarray) -> np.ndarray:
    """
    Crops the image to a 400x400 square from the center and converts it to
    grayscale.

    Parameters:
        img (np.ndarray): Original RGB image.

    Returns:
        np.ndarray: Grayscale cropped image with shape (400, 400)
    """
    try:
        if img is None:
            raise ValueError("Image data is None")

        height, width = img.shape[0], img.shape[1]

        # Define crop size and use it consistently
        crop_size = 400
        half_crop = crop_size // 2
        cx, cy = width // 2, height // 2

        cropped = img[
            cy - half_crop:cy + half_crop,
            cx - half_crop:cx + half_crop
        ]

        if cropped.ndim == 3:
            gray = np.mean(cropped, axis=2).astype(np.uint8)
        else:
            gray = cropped

        print(
            f"The shape of image is: "
            f"{gray.shape + (1,) if gray.ndim == 2 else gray.shape}"
        )
        print(gray[..., np.newaxis])
        return gray

    except Exception as e:
        print(f"Error in crop_and_gray: {e}")
        return None


def manual_transpose(arr: np.ndarray) -> np.ndarray:
    """
    Manually transposes a 2D grayscale numpy array (no NumPy functions).

    Parameters:
        arr (np.ndarray): Grayscale image of shape (H, W)

    Returns:
        np.ndarray: Transposed image of shape (W, H)
    """
    try:
        if arr is None:
            raise ValueError("No data to transpose")

        height = len(arr)
        width = len(arr[0])

        # Initialize empty transposed array
        transposed = [[0 for _ in range(height)] for _ in range(width)]

        # Transpose manually by swapping indices
        for i in range(height):
            for j in range(width):
                transposed[j][i] = arr[i][j]

        result = np.array(transposed, dtype=np.uint8)
        print(f"New shape after Transpose: {result.shape}")
        print(result)
        return result

    except Exception as e:
        print(f"Error in manual_transpose: {e}")
        return None


def display_image(img: np.ndarray) -> None:
    """
    Displays a grayscale image using matplotlib.

    Parameters:
        img (np.ndarray): Image to display.
    """
    try:
        plt.imshow(img, cmap='gray')
        plt.title("Transposed Grayscale Image")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    """
    Main entry point for rotating the image.
    """
    try:
        original = ft_load("../animal.jpeg")
        cropped_gray = crop_and_gray(original)
        transposed = manual_transpose(cropped_gray)
        display_image(transposed)
    except Exception as e:
        print(f"Unexpected error in main: {e}")


if __name__ == "__main__":
    main()
