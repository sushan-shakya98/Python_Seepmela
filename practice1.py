# Exercise 1 (Easy – Even/Odd)

# 👉 Write a Python program:

# Take a number (you can assign it like num = 7)
# Print:
# "Even" if number is even
# "Odd" if number is odd

# num = 7
# if(num % 2 ==0):
#     print("The number is even")
# else:
#     print("The number is odd")

# Exercise 2 (Comparison + If)

# 👉 Write a program:

# Take two numbers
# Print which one is greater
# If equal → print "Both are equal"

# num1 = float(input("Enter the First number: "))
# num2 = float(input("Enter the Second number: "))
# if(num1>num2 or num2<num1):
#     print("Num1 is greater than num2")
# elif(num2>num1 or num1<num2):
#     print("Num2 is greater than num1")
# else:
#     print("The number is equal")

# Exercise 3 (Logical Operator)

# 👉 Write a program:

# Take age
# If age is between 18 and 60 → print "Eligible to work"
# Otherwise → "Not eligible"

# age = int(input("Enter your age for the vacancy: "))
# if(age>=18 and age<=60):
#     print("Elgible for work")
# else:
#     print("Not Eligible")

# Exercise 4 (Real-life – Your Gold Shop 💍)

# 👉 Write a program:

# Take amount
# Apply discount:
# Above 5000 → "20% discount"
# Above 3000 → "10% discount"
# Otherwise → "No discount"

# Amount = float(input("Enter the value for discount: "))
# if(Amount >= 5000):
#     print("You gad 20% Discount")
# elif(Amount >= 3000 and Amount <= 3000):
#     print("You gad 10% Discount")
# else:
#     print("No Discount")

# Exercise 5 (Bonus – Password Check 🔐)

# 👉 Write a program:

# Set password = "admin123"
# Take input (or assign variable)
# If correct → "Access granted"
# Else → "Access denied"

# password = "admin123"
# user_input = input("Enter Password: ")
# if user_input == password:
#     print("Access Granted")
# else:
#     print("Access denied")

# num = float(input("enter number"))
# if (num > 0):
#     print("Positive")
# elif (num < 0):
#     print("negative")
# else:
#     print("Zer0")

# Program 2: Largest of 3 numbers
# Write it and send 👍

num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))
num3 = float(input("Enter 3rd number"))
if (num1 > num2 and num1 > num3):
    print("Num1 is greater")
elif (num2 > num1 and num2 > num3):
    print("Num2 is greater")
else:
    print("Num3 is greater")
    


    
    
    