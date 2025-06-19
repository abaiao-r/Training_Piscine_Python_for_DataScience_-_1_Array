import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.

    Parameters:
        array (np.ndarray): Original image array.

    Returns:
        np.ndarray: Color-inverted image.
    """
    try:
        inverted = 255 - array  # using only -, =
        plt.imshow(inverted)
        plt.title("Inverted Image")
        plt.show()
        return inverted
    except Exception as e:
        print(f"Error in ft_invert: {e}")
        return array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Filters the image to keep only the red channel.

    Parameters:
        array (np.ndarray): Original image array.

    Returns:
        np.ndarray: Image with only red channel preserved.
    """
    try:
        red = array.copy()
        red[:, :, 1] *= 0  # Green
        red[:, :, 2] *= 0  # Blue
        plt.imshow(red)
        plt.title("Red Filter")
        plt.show()
        return red
    except Exception as e:
        print(f"Error in ft_red: {e}")
        return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Filters the image to keep only the green channel.

    Parameters:
        array (np.ndarray): Original image array.

    Returns:
        np.ndarray: Image with only green channel preserved.
    """
    try:
        green = array.copy()
        green[:, :, 0] -= green[:, :, 0]  # Red
        green[:, :, 2] -= green[:, :, 2]  # Blue
        plt.imshow(green)
        plt.title("Green Filter")
        plt.show()
        return green
    except Exception as e:
        print(f"Error in ft_green: {e}")
        return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Filters the image to keep only the blue channel.

    Parameters:
        array (np.ndarray): Original image array.

    Returns:
        np.ndarray: Image with only blue channel preserved.
    """
    try:
        blue = array.copy()
        blue[:, :, 0] = 0  # Red
        blue[:, :, 1] = 0  # Green
        plt.imshow(blue)
        plt.title("Blue Filter")
        plt.show()
        return blue
    except Exception as e:
        print(f"Error in ft_blue: {e}")
        return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale using average method.

    Parameters:
        array (np.ndarray): Original image array.

    Returns:
        np.ndarray: Grayscale image.
    """
    try:
        grey = array.copy()
        # Manual average using /
        average = (grey[:, :, 0] / 3 + grey[:, :, 1] /
                   3 + grey[:, :, 2] / 3).astype(np.uint8)
        grey[:, :, 0] = average
        grey[:, :, 1] = average
        grey[:, :, 2] = average
        plt.imshow(grey)
        plt.title("Greyscale Filter")
        plt.show()
        return grey
    except Exception as e:
        print(f"Error in ft_grey: {e}")
        return array

# ╔════════════════════════════════════════════════════════════════════╗
# ║                        IMAGE FILTER MATH SUMMARY                  ║
# ╠══════════════╦════════════════════════════╦═══════════════════════╣
# ║  Function    ║         Goal               ║      Math Used        ║
# ╠══════════════╬════════════════════════════╬═══════════════════════╣
# ║ ft_invert    ║ Reverse brightness         ║ 255 - value           ║
# ║ ft_red       ║ Keep only Red channel      ║ G *= 0, B *= 0        ║
# ║ ft_green     ║ Keep only Green channel    ║ R -= R, B -= B        ║
# ║ ft_blue      ║ Keep only Blue channel     ║ R = 0, G = 0          ║
# ║ ft_grey      ║ Convert to Greyscale       ║ (R + G + B) / 3       ║
# ║              ║                            ║ Set R=G=B=avg         ║
# ╚══════════════╩════════════════════════════╩═══════════════════════╝

# ─────────────────────────────────────────────────────────────────────
# 🎨 Color image pixels are like this:
# Each pixel has 3 channels → [R, G, B]
# For example: [120, 90, 60]
# ─────────────────────────────────────────────────────────────────────

# 🔄 ft_invert — Inverts the color
# Formula: 255 - value
# Example:
#   Original: [120, 90, 60]
#             ↓↓↓↓↓↓↓↓↓↓↓↓↓
#   Inverted: [135, 165, 195]
#   Because:  255 - 120 = 135
#             255 - 90  = 165
#             255 - 60  = 195

# 🔴 ft_red — Keep only the Red channel
# Formula:
#   G *= 0
#   B *= 0
# Example:
#   Original: [120, 90, 60]
#             ↓↓↓↓↓↓↓↓↓↓↓↓↓
#   Red only: [120, 0, 0]

# 🟢 ft_green — Keep only the Green channel
# Formula:
#   R -= R
#   B -= B
# Example:
#   Original: [120, 90, 60]
#             ↓↓↓↓↓↓↓↓↓↓↓↓↓
#   Green:    [0, 90, 0]

# 🔵 ft_blue — Keep only the Blue channel
# Formula:
#   R = 0
#   G = 0
# Example:
#   Original: [120, 90, 60]
#             ↓↓↓↓↓↓↓↓↓↓↓↓↓
#   Blue:     [0, 0, 60]

# ⚫ ft_grey — Convert to Greyscale
# Formula:
#   Grey = (R + G + B) / 3
# Then set all 3 channels to the average
# Example:
#   Original: [120, 90, 60]
#   Average:  (120 + 90 + 60) / 3 = 90
#   Grey:     [90, 90, 90]

# ─────────────────────────────────────────────────────────────────────
# 🧠 Full Flow Visualization:
#   Original      Red        Green      Blue       Invert      Greyscale
#   [120,90,60] → [120,0,0] [0,90,0] → [0,0,60] → [135,165,195] → [90,90,90]
# ─────────────────────────────────────────────────────────────────────
