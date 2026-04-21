import random

random_number = random.randint(10,15)
guess_attempt = 5

count = 0

while True:
    user_input = input("Enter Number: ")
    count += 1

    if user_input == str(random_number):
        print(f'Number match in {count} times')
        play = input("Do you want to play again? y/n ").lower()
        if play == 'y':
            random_num = random.randint(10,15)
            count = 0
        
        else:
            print("Thank you for Playing")
            break
    
    else:
        guess_attempt -= 1
        
        print(f'You have {guess_attempt} attempt left')
        if guess_attempt <= 0:
            break
        print("Try Again!!")
