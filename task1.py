import random

choices = ["rock", "paper", "scissor"]

player_score = 0
computer_score = 0

while player_score < 50 and computer_score < 50:
    player = input("Enter rock, paper, scissor : ").lower()

    if player not in choices:
        print("Invalid choices, Try again")
        continue

    computer = random.choice(choices)
    print("Computer chose: ", computer)

    if player == computer:
        print("Its a draw")

    elif (player == "paper" and computer == "rock") or \
            (player == "scissor" and computer == "paper") or \
            (player == "rock" and computer == "scissor"):
            print("Player wins!!")
            player_score += 5
    
    else:
        print("Computer wins!!")
        computer_score += 5
    
    print("Player score: ", player_score, "|| Computer score: ", computer_score)

if player_score > 50:
     print("Players wins!!, CONGRATULATIONS")
else:
     print("Computer wins!!,CONGRATULATIONS")
         