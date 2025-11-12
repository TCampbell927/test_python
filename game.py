import random
print("Welcome to Rock-Paper-Scissors!")

player_input = input("Choose rock, paper, or scissors: ")
print(f"You chose: {player_input}")

computer_choice = random.choice(["rock", "paper", "scissors"])
print(f"Computer chose: {computer_choice}")