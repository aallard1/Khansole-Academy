"""
Prints out a spaceship launch sequence.
"""

def main():
    x = 10
    count = x
    print(count)
    for i in range(9):
        # Subtracts 1 from the count variable
        count -= 1
        # Prints current count value
        print(count)
        # Subtracts 1 from the x variable
        x -= 1
    print("Liftoff!")

if __name__ == '__main__':
    main()