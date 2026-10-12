from utils import (
    square,
    is_even,
    celsius_to_fahrenheit,
    greet,
)


def main():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Student"

    print(greet(name))

    try:
        number = float(input("Enter a number: "))
        print(f"Square: {square(number)}")
        print(f"Parity: {'Even' if is_even(number) else 'Odd'}")
        print(
            f"Fahrenheit equivalent: "
            f"{celsius_to_fahrenheit(number):.2f}°F"
        )
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()