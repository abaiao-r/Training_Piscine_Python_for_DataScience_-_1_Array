from load_image import ft_load
from zoom import zoom_and_display

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def print_result(test_name, passed):
    status = f"{GREEN}PASSED{RESET}" if passed else f"{RED}FAILED{RESET}"
    print(f"{test_name}: {status}")


def test_valid_jpeg_zoom():
    print("Test 1: Valid JPEG file and zoom")
    arr = ft_load("../animal.jpeg")
    if arr is not None:
        try:
            zoom_and_display(arr)
            print_result("Test 1", True)
        except Exception as e:
            print(f"Error during zoom_and_display: {e}")
            print_result("Test 1", False)
    else:
        print_result("Test 1", False)


def test_nonexistent_file():
    print("\nTest 2: Non-existent file")
    arr = ft_load("notfound.jpg")
    print_result("Test 2", arr is None)


def test_unsupported_format():
    print("\nTest 3: Unsupported format (PNG)")
    arr = ft_load("../some.png")
    print_result("Test 3", arr is None)


def test_corrupted_file():
    print("\nTest 4: Corrupted file")
    arr = ft_load("../corrupted.jpg")
    print_result("Test 4", arr is None)


def main():
    test_valid_jpeg_zoom()
    test_nonexistent_file()
    test_unsupported_format()
    test_corrupted_file()


if __name__ == "__main__":
    main()
