"""Simple calculator program with basic arithmetic operations."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # Division by zero
    return a / b


def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    print("Calculator")
    print("-" * 20)
    for key, (name, _) in operations.items():
        print(f"  {key}. {name}")
    print("-" * 20)

    choice = input("Select operation (1-4): ").strip()
    if choice not in operations:
        print("Invalid choice.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number.")
        return

    name, func = operations[choice]
    result = func(num1, num2)

    if result is None:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {num1} {name} {num2} = {result}")


if __name__ == "__main__":
    main()
