from array2D import slice_me
import difflib
import sys
import io


def print_result(test_name, passed):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    status = f"{GREEN}PASSED{RESET}" if passed else f"{RED}FAILED{RESET}"
    print(f"{test_name}: {status}")


def test_slice_me_valid():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    try:
        result1 = slice_me(family, 0, 2)
        result2 = slice_me(family, 1, -2)
        expected1 = [[1.8, 78.4], [2.15, 102.7]]
        expected2 = [[2.15, 102.7]]
        return result1 == expected1 and result2 == expected2
    except Exception:
        return False


def test_not_a_list():
    try:
        slice_me("not a list", 0, 2)
        return False
    except Exception:
        return True


def test_not_list_of_lists():
    try:
        slice_me([1.80, 78.4, 2.15, 102.7], 0, 2)
        return False
    except Exception:
        return True


def test_rows_different_lengths():
    try:
        slice_me([[1.80, 78.4], [2.15], [2.10, 98.5]], 0, 2)
        return False
    except Exception:
        return True


def test_empty_list():
    try:
        slice_me([], 0, 2)
        return False
    except Exception:
        return True


def test_slice_me_example_case():
    """
    Test the example case from the subject and check output.
    """
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    expected_output = (
        "My shape is : (4, 2)\n"
        "My new shape is : (2, 2)\n"
        "[[1.8, 78.4], [2.15, 102.7]]\n"
        "My shape is : (4, 2)\n"
        "My new shape is : (1, 2)\n"
        "[[2.15, 102.7]]\n"
    )

    buf = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buf
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    finally:
        sys.stdout = sys_stdout
    result = buf.getvalue()

    passed = result == expected_output
    print_result("Test example case output", passed)
    print("=== Actual Output ===")
    print(result)
    print("=== Expected Output ===")
    print(expected_output)
    print("=== Diff ===")
    diff = list(difflib.unified_diff(
        expected_output.splitlines(keepends=True),
        result.splitlines(keepends=True),
        fromfile='expected',
        tofile='actual'
    ))
    if diff:
        print(''.join(diff))
    else:
        print("No differences found.")


def main():
    print_result("Test valid input", test_slice_me_valid())
    print_result("Test not a list", test_not_a_list())
    print_result("Test not list of lists", test_not_list_of_lists())
    print_result("Test rows of different lengths",
                 test_rows_different_lengths())
    print_result("Test empty list", test_empty_list())
    test_slice_me_example_case()


if __name__ == "__main__":
    main()
