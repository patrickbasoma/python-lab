from utils import square, is_even, celsius_to_fahrenheit


def main():
    number = float(input("Enter a number: "))

    print(f"Square: {square(number)}")
    print(f"Parity: {'Even' if is_even(number) else 'Odd'}")
    print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(number):.2f}°F")


if __name__ == "__main__":
    main()