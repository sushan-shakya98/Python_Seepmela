# a = [1,2,3,4, "hello", "test",1,2,4, 7.3, True]
# for i in a:
#     if isinstance(i, bool):
#         continue
#     if isinstance(i, str):
#         continue
#     print(i)

# Filter Integers
# Given a mixed list, print only integers (you already tried something similar—now do it with continue and a while loop).
# a = [1,2,3,4, "hello", "test",1,2,4, 7.3, True]
# i = 0
# while i < len(a):
    
#     if isinstance(a[i], bool):
#         i += 1
#         continue
#     if isinstance(a[i], int):
#         print(a[i])
#     i += 1

# Palindrome Checker
# Check if a string is the same forward and backward.
# s = input("Enter a word: ")
# if (s == s[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Count Vowels
# Input: string
# Output: number of vowels

# s = input("Enter word or sentences: ")
# vowels = "aeiou"
# count = 0

# for ch in s:
#     if ch.lower() in vowels:
#         count += 1

# print(count)



# FizzBuzz
# Classic: print 1–100
# Multiples of 3 → "Fizz", 5 → "Buzz", both → "FizzBuzz"
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Find Maximum Without max()
# From a list of numbers
# nums = [3, 7, 2, 9, 5]

# max_num = nums[0]

# for n in nums:
#     if n > max_num:
#         max_num = n

# print(max_num)

# Two Sum Problem
# Given a list and target, return indices of numbers that add up to target.
# nums = [2, 7, 11, 15]
# target = 9

# d = {}

# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in d:
#         print(d[diff], i)
#     d[nums[i]] = i

# Remove Duplicates
# From a list without using set
# nums = [1, 2, 2, 3, 4, 4, 5]
# result = []

# for n in nums:
#     if n not in result:
#         result.append(n)

# print(result)

# Word Frequency Counter
# Count how many times each word appears in a sentence.
# s = "hello world hello"
# words = s.split()

# freq = {}

# for w in words:
#     if w in freq:
#         freq[w] += 1
#     else:
#         freq[w] = 1

# print(freq)

# Anagram Checker
# Check if two strings contain the same characters.
# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


# Prime Number Generator
# Print all primes up to n
# n = 20

# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

'''
Advanced (interview-level thinking)

Focus: efficiency, algorithms

Binary Search (from scratch)
Merge Two Sorted Lists
Longest Substring Without Repeating Characters
Valid Parentheses Problem
Sorting Algorithms
Implement Bubble, Selection, and Quick Sort manually
🔹 Real-World Mini Projects (VERY important 🚀)

This is where you actually grow faster.

CLI To-Do App
Add / delete / view tasks
Expense Tracker
Store transactions in a file
Password Generator
Random strong passwords
Simple Calculator
Handle +, -, *, /
Contact Book
Save and search contacts
'''



