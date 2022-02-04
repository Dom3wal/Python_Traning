from msilib.schema import Complus
import random
from secrets import choice

choices = ["rock", "paper", "scissors"]
while 1:
    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Choose one option: rock, papper, scissors ").lower()

    if player == computer:
        print("Player: " + player)
        print("Computer: "+ computer)
        print("TIE")
    elif player == 'rock':
        if computer == "paper":
            print("Player " + player)
            print("Computer: "+ computer)
            print("We lost")
        if computer == "scissors":
            print("Player: " + player)
            print("Computer: "+ computer)
            print("We lost")
    else:
        print("somethingf esle has been chosen")
    play_again = input("Play again, Yes or No ").lower()
    if play_again != "yes":
        break

print("Bye")