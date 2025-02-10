# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial_recursive(number - 1)

def main():
    print("Factorial Computation Using Recursion")

    while True:
        try:
            number = int(input("Enter a non-negative integer: "))

        # handle negative input
            if number < 0:
                print("Error! To determine factorial, the number must be positive.")
            else:
                break

        except ValueError:
            print("Error! Please enter a valid number")

    # Call factorial_recursive method
    result = factorial_recursive(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()