from load_image import ft_load


def main():
    """
    Manual test function.
    """
    result = ft_load("../landscape.jpg")
    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
