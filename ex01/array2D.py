import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of the 2D array, slices it, prints the new shape,
    and returns the sliced array as a list.

    Args:
        family (list): 2D list representing the array.
        start (int): Start index for slicing.
        end (int): End index for slicing.

    Returns:
        list: Sliced 2D array as a list.

    Raises:
        ValueError: If input is not a 2D list with rows of equal length.
    """
    arr = np.array(family)
    if arr.ndim != 2:
        raise ValueError(
            "Input must be a 2D array (list of lists with equal lengths).")
    print(f"My shape is : {arr.shape}")
    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()
