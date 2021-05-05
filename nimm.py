"""
Game of Nimm
Users take turns drawing one or two stones from the pile.
The last player to remove stones loses.
"""

import random

def pick_stones():
    num_stones = 20
    player_turn = 1
    while num_stones >= 0:
        if player_turn == 1:
            print(f"There are {num_stones} stones left")
            player_choice = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while player_choice >= 3 or player_choice < 1:
                player_choice = check_input(player_choice)
            num_stones -= player_choice
            player_turn = 2
            print('')
            if num_stones == 0 or num_stones < 0:
                who_won = check_winner(player_turn)
                quit()
        if player_turn == 2:
            print(f"There are {num_stones} stones left")
            player_choice = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while player_choice >= 3 or player_choice < 1:
                player_choice = check_input(player_choice)
            num_stones -= player_choice
            player_turn = 1
            print('')
            if num_stones == 0 or num_stones < 0:
                who_won = check_winner(player_turn)
                quit()
    return num_stones

def check_input(player_choice):
    player_choice = int(input("Please enter 1 or 2: "))
    return player_choice

def check_winner(player_turn):
    if player_turn == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

def main():
    num_stones = 20
    pick_stones()

if __name__ == '__main__':
    main()