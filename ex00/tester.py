from give_bmi import give_bmi, apply_limit


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))

        limit_check = apply_limit(bmi, 26)
        print(limit_check)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
