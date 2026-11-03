def Calculate(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    return a + b


def main():
    print("py Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = Calculate(a, b)
        print("Result:", result)
    except (ValueError, TypeError, ZeroDivisionError) as error:
        print("Error:", error)


if __name__ == "__master__":
    main()