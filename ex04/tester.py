from load_image import ft_load
from rotate import crop_and_gray, manual_transpose, display_image

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def print_result(test_name, success):
    color = GREEN if success else RED
    status = "Success" if success else "Failed"
    print(f"{test_name}: {color}{status}{RESET}\n")


def test_ft_load():
    print("Testing ft_load...")
    arr = ft_load("../animal.jpeg")  # Update path if needed
    print_result("ft_load", arr is not None)
    return arr


def test_crop_and_gray(arr):
    print("Testing crop_and_gray...")
    cropped = crop_and_gray(arr)
    success = (
        cropped is not None
        and cropped.ndim == 2
        and cropped.shape == (400, 400)
    )
    print_result("crop_and_gray", success)
    return cropped


def test_manual_transpose(arr):
    print("Testing manual_transpose...")
    transposed = manual_transpose(arr)
    success = transposed is not None and transposed.shape == (400, 400)
    print_result("manual_transpose", success)
    return transposed


def main():
    arr = test_ft_load()
    if arr is not None:
        cropped = test_crop_and_gray(arr)
        if cropped is not None:
            transposed = test_manual_transpose(cropped)
            if transposed is not None:
                display_image(transposed)


if __name__ == "__main__":
    main()
