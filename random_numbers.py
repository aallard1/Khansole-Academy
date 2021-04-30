"""
Prints out 10 random numbers between 0 and 100.
"""

import random

MIN_RANDOM = 0
MAX_RANDOM = 100
NUM_RANDOM = 10

def main():
    for i in range(NUM_RANDOM):
        # Generates a pseudorandom integer value between MIN_RANDOM and MAX_RANDOM, inclusively
        num_rand = random.randint(MIN_RANDOM, MAX_RANDOM)
        # Prints the value
        print(num_rand)

if __name__ == '__main__':
    main()