# import random

# playerScore = 0
# computerScore = 0

# choices = ["r", "p", "s"]
# data = random.choice(choices)
# print(data)

# while True:
#     user_data = input('Enter, r, p, s : ')
#     if user_data not in choices:
#         print("invalid choice")
#         continue
#     print("correct input")
#     if data == user_data:
#         print("Game Draw")

import random

player_score = 0
computer_score = 0

choices = ["r","p","s"]

while player_score < 50 and computer_score < 50:
    player = input("Enter r,p,s: ").lower()

    if player not in choices:
        print("invalid choice, Try Again!!")
        continue

    computer = random.choice(choices)
    print("Computer chose: ", computer)

    if player == computer:
        print("Draw")

    elif (player == "r" and computer == "s") or \
            (player == "s" and computer == "p") or \
            (player == "p" and computer == "r"):
            print("Player win this Round")
            player_score += 5

    else:
        print("Computer win this Round")
        computer_score += 5
    
    print("Score -> You:", player_score, "| Computer:", computer_score)

# Final winner
if player_score >= 50:
    print("Congratulations! You won the game!")
else:
    print("Computer wins the game. Better luck next time!")