from load_image import ft_load

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def print_result(test_name, passed):
    status = f"{GREEN}PASSED{RESET}" if passed else f"{RED}FAILED{RESET}"
    print(f"{test_name}: {status}")


def test_valid_jpeg():
    print("Test 1: Valid JPEG file")
    result = ft_load("../landscape.jpg")
    print_result("Test 1", result is not None)


def test_nonexistent_file():
    print("\nTest 2: Non-existent file")
    result = ft_load("notfound.jpg")
    print_result("Test 2", result is None)


def test_unsupported_format():
    print("\nTest 3: Unsupported format (PNG)")
    result = ft_load("../some.png")
    print_result("Test 3", result is None)


def test_corrupted_file():
    print("\nTest 4: Corrupted file")
    result = ft_load("../corrupted.jpg")
    print_result("Test 4", result is None)


def main():
    test_valid_jpeg()
    test_nonexistent_file()
    test_unsupported_format()
    test_corrupted_file()


if __name__ == "__main__":
    main()
