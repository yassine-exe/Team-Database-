
def calculate(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    return a + b


def main():
    print("Python Calculator")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = calculate(a, b)
        print("Result:", result)

    except (ValueError, TypeError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
