"""
Prompts the user for their name and then says hello!
"""

def main():
    # Asks user for their name and stores the user input in the variable user_name with type string
    user_name = str(input("What is your name? "))
    # Prints Hello followed by the user's input
    print(f"Hello {user_name}!")

if __name__ == '__main__':
    main()