"""
Prompts the user to answer simple addition problems 
until the user answers three correct in a row.
"""

import random

NUM_CORRECT = 3

def main():
    num_correct = 0
    while num_correct <= NUM_CORRECT:
        num_correct = addition_prob(num_correct)
        if num_correct == NUM_CORRECT:
            print("Congratulations! You mastered addition.")
            quit()

def addition_prob(num_correct):
    num_1 = random.randint(10, 99)
    num_2 = random.randint(10, 99)
    correct_answer = num_1 + num_2
    print(f"What is {num_1} + {num_2}?")
    user_answer = int(input("Your answer: "))
    if user_answer == correct_answer:
        num_correct += 1
        print(f"Correct! You've gotten {num_correct} correct in a row.")
        return num_correct
    else:
        num_correct = 0
        print(f"Incorrect. The expected answer is {correct_answer}")
        return num_correct

if __name__ == '__main__':
    main()