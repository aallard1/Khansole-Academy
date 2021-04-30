"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    # Prompts user to enter a number, which is stored as a float inside the variable first_num
    first_num = float(input("Enter first number: "))
    # Prompts user to enter another number, which is stored as a float inside the variable second_num
    second_num = float(input("Enter second number: "))
    # Stores the result of the mathematical operation in the variable subtract as a float
    subtract = first_num - second_num
    # Prints the result of the calculation
    print(f"The result is {subtract}")

if __name__ == '__main__':
    main()