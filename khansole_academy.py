"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    # Generates a pseudorandom integer value between 10 and 99, inclusively
    num_1 = random.randint(10, 99)
    # Generates another pseudorandom integer value between 10 and 99, inclusively
    num_2 = random.randint(10, 99)
    # Adds the two numbers together and stores the value in correct_answer as an int
    correct_answer = num_1 + num_2
    print(f"What is {num_1} + {num_2}?")
    # Stores user input in variable user_answer as an int
    user_answer = int(input("Your answer: "))
    # Checks if user_answer is equivalent to correct_answer
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The expected answer is {correct_answer}")

if __name__ == '__main__':
    main()