from load_image import ft_load
from pimp_image import (
    ft_invert,
    ft_red,
    ft_green,
    ft_blue,
    ft_grey
)


def main():
    """
    Main function to test all color filters on landscape.jpg.
    """
    try:
        array = ft_load("../landscape.jpg")

        if array is None:
            raise ValueError("Image not loaded properly.")

        # Run all filter functions
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

        # Print docstring of ft_invert
        print(ft_invert.__doc__)

    except Exception as e:
        print(f"Fatal error in tester: {e}")


if __name__ == "__main__":
    main()
