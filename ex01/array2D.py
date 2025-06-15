
def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D list and returns a sliced version using slicing.

    Args:
        family (list): 2D list (list of lists) where each sublist has the same
        size.
        start (int): Start index for slicing (inclusive).
        end (int): End index for slicing (exclusive).

    Returns:
        list: Sliced 2D list from start to end rows.

    Raises:
        TypeError: If family is not a list of lists or contains non-list
        elements.
        ValueError: If rows are not all the same length or if start/end indices
        are invalid.
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list.")
    if len(family) == 0:
        raise ValueError("family cannot be empty.")
    row_length = None
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a 2D list (list of lists).")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise ValueError("All rows must be of the same length.")
    # Print original shape
    print(f"My shape is : ({len(family)}, {row_length})")

    # Validate slicing indices
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers.")

    # Slice the family list rows using start:end
    sliced_family = family[start:end]

    # Print new shape
    print(f"My new shape is : ({len(sliced_family)}, {row_length})")

    return sliced_family
