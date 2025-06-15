def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[float]:
    """
    Calculate BMI values from lists of heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of BMI values calculated as weight / (height ** 2).

    Raises:
        TypeError: If inputs are not lists of int or float.
        ValueError: If lists are of different lengths or contain invalid values
        (zero or negative height).
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be the same length.")
    for h, w in zip(height, weight):
        if not (isinstance(h, (int, float)) and isinstance(w, (int, float))):
            raise TypeError(
                "All elements in height and weight must be int or float.")
        if h <= 0:
            raise ValueError(
                "Height values must be greater than zero to calculate BMI.")
        if w <= 0:
            raise ValueError(
                "Weight values must be greater than zero to calculate BMI.")
    bmi_values = [w / (h ** 2) for h, w in zip(height, weight)]
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine if each BMI value exceeds a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Threshold limit.

    Returns:
        list[bool]: List of booleans where True indicates BMI above the limit.

    Raises:
        TypeError: If bmi is not a list of int or float, or limit is not an
        int.
    """
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list.")
    if not isinstance(limit, int):
        raise TypeError("limit must be an int.")
    for val in bmi:
        if not isinstance(val, (int, float)):
            raise TypeError("All elements in bmi list must be int or float.")
    return [val > limit for val in bmi]
