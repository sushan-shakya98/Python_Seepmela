import random

# random_number = random.randint(10,12)
# print("This is random number", random_number)
# count = 0

# while True:
#     user_input = int(input("Enter the number: "))
#     count += 1

#     if user_input == random_number:
#         print(f"Number Match in {count} times")
#         break
#     else:
#         print("Try again!!")



# random_number = random.randint(10,12)
# count = 0

# while True:
#     user_input = input("Enter the number: ")
#     count += 1
    
#     if user_input == str(random_number):
#         print(f"Number Match in {count} times")
#         play = input("Do you want to play again? y/n ").lower()
#         if play == 'y':
#             random_num = random.randint(10,12)
#             count = 0 
#         else:
#             print("Thank you for playing")
#             break
#     else:
#         print("Try Again!!")



random_number = random.randint(10,12)
guess_attempt = 5

count = 0

while True:
    user_input = input("Enter the number: ")
    count += 1
    
    if user_input == str(random_number):
        print(f"Number Match in {count} times")
        play = input("Do you want to play again? y/n ").lower()
        if play == 'y':
            random_num = random.randint(10,12)
            count = 0 
        else:
            print("Thank you for playing")
            break
    else:
        guess_attempt -= 1

        print(f'You have {guess_attempt} attempt left')
        if guess_attempt <= 0 :
            break
        print("Try Again!!")




# score 5 should be added to player or computer and if the total scores is 50 the player wins

    
