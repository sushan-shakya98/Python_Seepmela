import random


# print(random.random())//gives values in decimal from 0-1
# print(random.random()*100) //multiplies with random value from 0-1
# print(random.randint(10,20)) // gives random integer value

# a = ["hello", "yesy", "test", "namaste"]
# print(random.choice(a)) //gives random choice selection from the list a

# Task 1
# write a program for Guess the number using random.randint(10,50)\


random_number = random.randint(10,50)

while True:
    user_input = int(input("Enter random number from 10 - 50: "))
    if user_input != random_number:
        print("You guess the wrong number")
        
    else:
        print("You guess the right number")
