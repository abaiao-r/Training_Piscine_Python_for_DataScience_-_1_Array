import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_and_display(img: np.ndarray) -> None:
    """
    Extracts a center 400x400 region and displays it in grayscale with axes.

    Parameters:
        img (np.ndarray): The original color image.
    """
    try:
        if img is None:
            raise ValueError("No image data to process.")

        # Get image dimensions
        height, width = img.shape[0], img.shape[1]
        channels = img.shape[2] if img.ndim == 3 else 1
        print(f"Image dimensions: {width}x{height}")
        print(f"Number of channels: {channels}")

        # Choose center crop for zoom: 400x400
        center_x, center_y = width // 2, height // 2
        half_crop = 200
        cropped = img[center_y - half_crop:center_y + half_crop,
                      center_x - half_crop:center_x + half_crop]

        # Convert to grayscale (if not already)
        if cropped.ndim == 3:
            gray = np.mean(cropped, axis=2).astype(np.uint8)
        else:
            gray = cropped

        # Add extra dimension for shape printing if needed
        zoomed = gray[..., np.newaxis]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # Display image using matplotlib
        plt.imshow(gray, cmap='gray', extent=[0, 400, 0, 400])
        plt.title("Zoomed Image (Center 400x400)")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.grid(False)
        plt.show()

    except Exception as e:
        print(f"Error during zoom or display: {e}")


def main():
    """
    Main function to load an image and zoom into it.
    Handles all potential errors gracefully.
    """
    try:
        img_array = ft_load("../animal.jpeg")
        zoom_and_display(img_array)
    except Exception as e:
        print(f"Unexpected error in main: {e}")


if __name__ == "__main__":
    main()
