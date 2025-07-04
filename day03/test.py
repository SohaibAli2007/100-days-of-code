#rock paper scissors 
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    global player_choice
    player_choice = player

    global computer_choice
    computer_choice = computer

    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "scissors" and computer == "rock":
        return "Computer Wins!"
    elif player == "paper" and computer == "rock":
        return "You Win!"
    elif player == "rock" and computer == "scissors":
        return "You Win!"
    elif player == "rock" and computer == "paper":
        return "Computer Wins!"

    




