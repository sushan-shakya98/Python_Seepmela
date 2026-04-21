# # a = [1, 2]
# # b = [3, 4]

# # a.append(b)
# # print(a)

# # a = [1, 2]
# # a.extend(b)
# # print(a)

# #output [1, 2, [3, 4]] and [1, 2, 3, 4]


# a = [1, 2, 3, 4, 3]

# del a[1]
# print(a)

# a.remove(3)
# print(a)

# x = a.pop()
# print(a, x)

# # output [1, 4] 3

# 🔹 Question 1: Basic List + Append
# a = [1, 2, 3]
# a.append(4)
# print(a)

# 👉 What will be the output?

# 🔹 Question 2: Insert vs Append
# a = [10, 20, 30]
# a.insert(1, 15)
# print(a)

# 👉 What does this print?

# 🔹 Question 3: Extend vs Append
# a = [1, 2]
# b = [3, 4]

# a.append(b)
# print(a)

# a = [1, 2]
# a.extend(b)
# print(a)

# 👉 What are the TWO outputs?

# 🔹 Question 4: List Slicing
# a = [0, 1, 2, 3, 4, 5]
# print(a[1:5:2])

# 👉 Output?

# 🔹 Question 5: Negative Slicing
# a = [10, 20, 30, 40, 50]
# print(a[-4:-1])

# 👉 Output?

# 🔹 Question 6: Delete vs Remove vs Pop
# a = [1, 2, 3, 4, 3]

# del a[1]
# print(a)

# a.remove(3)
# print(a)

# x = a.pop()
# print(a, x)

# 👉 What are the outputs step by step?

# 🔹 Question 7: Count and Index
# a = [1, 2, 3, 2, 4, 2]
# print(a.count(2))
# print(a.index(2))

# 👉 Output?

# 🔹 Question 8: Reverse vs Sort
# a = [3, 1, 4, 2]

# a.reverse()
# print(a)

# a.sort()
# print(a)

# 👉 Output?

# 🔹 Question 9: Clear
# a = [1, 2, 3]
# a.clear()
# print(a)

# 👉 Output?

# 🔹 Question 10: Trick Question (Important ⚠️)
# a = [1, 2, 3]
# b = a

# b.append(4)
# print(a)

# b = b + [5]
# print(a)

# 👉 Why does the second operation NOT affect a?

# If you want, I can:

# Check your answers
# Give harder interview-level questions
# Or 
# make a mini test (MCQs + coding)
# q1 answer will be  [1, 2, 3, 4]

# ✅ Correct.

# append(4) adds the element at the end of the same list, so:

# [1, 2, 3, 4]

# Ready for the next one?

# 👉 Q2: What will this print?

# a = [10, 20, 30]
# a.insert(1, 15)
# print(a)
# q2 answer is [10, 15,  20, 30]

# ✅ Yes — correct again.

# insert(1, 15) puts 15 at index 1, shifting the rest to the right:

# [10, 15, 20, 30]

# Let’s step it up a bit:

# 👉 Q3: What are the TWO outputs here?

# a = [1, 2]
# b = [3, 4]

# a.append(b)
# print(a)

# a = [1, 2]
# a.extend(b)
# print(a)
# one output will be [1,2,3,4]

# You’ve got one of them right, but you missed an important distinction.

# 👉 The second output (with extend) is:

# [1, 2, 3, 4]

# But the first output (with append) is different:

# [1, 2, [3, 4]]
# 🔑 Why?
# append(b) → adds the whole list as a single element
# extend(b) → adds each element individually

# So final answers:

# [1, 2, [3, 4]]
# [1, 2, 3, 4]

# Let’s see if you catch this one:

# 👉 Q4: What will this print?

# a = [0, 1, 2, 3, 4, 5]
# print(a[1:5:2])
# answer will be 3

# Not quite — this one trips people up.

# Let’s break it down:

# a = [0, 1, 2, 3, 4, 5]
# print(a[1:5:2])
# 🔍 Step-by-step:
# 1:5 → take elements from index 1 to 4 → [1, 2, 3, 4]
# :2 → take every 2nd element

# So:

# Start at index 1 → 1
# Skip one → take 3

# 👉 Final result:

# [1, 3]

# Your answer 3 would only be correct if it was a single index access — but slicing always returns a list.

# 👉 Try this next:

# Q5:

# a = [10, 20, 30, 40, 50]
# print(a[-4:-1])
# [30, 40, 50]

# Close — but slightly off.

# a = [10, 20, 30, 40, 50]
# print(a[-4:-1])
# 🔍 Convert negative indices:
# -4 → index 1 → 20
# -1 → index 4 → 50 (but excluded in slicing)

# So this becomes:

# a[1:4]  →  [20, 30, 40]

# 👉 Final answer:

# [20, 30, 40]

# You jumped ahead to [30, 40, 50], which would be something like:

# a[2:5]

# Let’s move on — this one mixes multiple concepts:

# 👉 Q6:

# a = [1, 2, 3, 4, 3]

# del a[1]
# print(a)

# a.remove(3)
# print(a)

# x = a.pop()
# print(a, x)
# [1, 3]

# That answer is way off — let’s go carefully step by step.

# a = [1, 2, 3, 4, 3]
# 🔹 Step 1: del a[1]

# Removes element at index 1 (2):

# [1, 3, 4, 3]
# 🔹 Step 2: a.remove(3)

# Removes the first occurrence of 3:

# [1, 4, 3]
# 🔹 Step 3: x = a.pop()
# pop() removes last element
# That element is 3

# So:

# a becomes → [1, 4]
# x becomes → 3
# ✅ Final outputs:
# [1, 3, 4, 3]
# [1, 4, 3]
# [1, 4] 3

# You answered [1, 3], which skips most of the operations. You need to track the list after each step — that’s the key skill here.

# 👉 Next one (easier, but important):

# Q7:

# a = [1, 2, 3, 2, 4, 2]
# print(a.count(2))
# print(a.index(2))
# answer will be 3 and 1

# ✅ Correct!

# Let’s verify:

# a = [1, 2, 3, 2, 4, 2]
# 🔹 count(2)

# Counts how many times 2 appears:

# appears at indices 1, 3, 5 → 3 times
# 🔹 index(2)

# Returns the first occurrence index:

# first 2 is at index 1
# ✅ Final output:
# 3
# 1

# You’re doing well now — this is exactly the kind of thinking needed for interviews.

# 👉 Next one (slightly tricky sorting behavior):

# Q8:

# a = [3, 1, 4, 2]

# a.reverse()
# print(a)

# a.sort()
# print(a)

# What’s the output?

# answer will be [2, 4, 1, 3] and then [1, 2, 3, 4]

# ✅ Perfect — correct.

# Step by step:

# 🔹 reverse()

# It just flips the list order (no sorting, just reversal):

# [2, 4, 1, 3]
# 🔹 sort()

# It arranges elements in ascending order:

# [1, 2, 3, 4]
# ✅ Final Answer:
# [2, 4, 1, 3]
# [1, 2, 3, 4]

# You’re getting consistent now 👍

# 👉 Next one (very easy but important):

# Q9:

# a = [1, 2, 3]
# a.clear()
# print(a)

# What will it print?

# []

# ✅ Correct.

# clear() removes all elements from the list, leaving it empty:

# []

# Final one — and this one checks your deep understanding 👇

# 👉 Q10 (Important):

# a = [1, 2, 3]
# b = a

# b.append(4)
# print(a)

# b = b + [5]
# print(a)

# 👉 What are the outputs, and why does the second operation NOT affect a?

# 1st the output will be [1, 2, 3, 4] and then new b will be formed because of  + sign so other output will be b = [1, 2, 3, 4, 5]

# You’re very close, but there’s one important correction.

# ✅ Step 1:
# b.append(4)
# print(a)

# ✔️ Correct:

# [1, 2, 3, 4]

# 👉 Because a and b point to the same list (same memory reference)

# ⚠️ Step 2:
# b = b + [5]
# print(a)

# You said:

# b = [1, 2, 3, 4, 5]

# ✔️ That part is correct for b

# BUT the question is: what happens to a?

# 👉 Output of print(a) is:

# [1, 2, 3, 4]
# 🔑 Why?
# append() → modifies the same list in-place
# b = b + [5] → creates a new list object and assigns it to b

# So now:

# a → still points to old list [1, 2, 3, 4]
# b → points to new list [1, 2, 3, 4, 5]
# 🧠 Key Concept:
# += → modifies existing list (like extend)
# + → creates new list
# ✅ Final outputs:
# [1, 2, 3, 4]
# [1, 2, 3, 4]

# If you want next:

# 🔥 Hard interview-level list questions
# 🧠 Trick questions (mutability, shallow vs deep copy)
# 💻 Mini coding test

# Just tell me 👍

# okay

# Good — let’s level this up 🔥
# Now I’ll give you interview-style tricky questions (these catch a lot of people).

# 🔥 Q1: += vs +
# a = [1, 2, 3]
# b = a

# b += [4]
# print(a)

# b = b + [5]
# print(a)

# 👉 What are the TWO outputs?

# 🔥 Q2: Slicing creates copy or not?
# a = [1, 2, 3, 4]
# b = a[:]

# b.append(5)
# print(a)
# print(b)

# 👉 What will be printed?

# 🔥 Q3: Nested List Trap
# a = [[1, 2], [3, 4]]
# b = a

# b[0].append(99)
# print(a)

# 👉 Output?

# 🔥 Q4: Shallow Copy Problem
# a = [[1, 2], [3, 4]]
# b = a[:]

# b[0].append(100)
# print(a)
# print(b)

# 👉 What are the outputs?

# 🔥 Q5: Reverse Slicing
# a = [1, 2, 3, 4, 5]
# print(a[::-1])
# print(a[3:0:-1])

# 👉 Two outputs?

# 🔥 Q6: Pop with Index
# a = [10, 20, 30, 40]

# x = a.pop(1)
# print(a, x)

# 👉 Output?

# 🔥 Q7: Remove vs Pop Error
# a = [1, 2, 3]

# a.remove(4)

# 👉 What happens?

# 🔥 Q8: Sorting Trick
# a = [3, 1, 2]
# b = a.sort()

# print(a)
# print(b)

# 👉 Output?

# 🔥 Q9: Index Error Trap
# a = [1, 2, 3]
# print(a.index(5))

# 👉 What happens?

# 🔥 Q10: List Multiplication Trap (VERY IMPORTANT)
# a = [[0]*3]*3

# a[0][0] = 1
# print(a)

# 👉 Output?

# Answer as many as you can — I’ll correct like an interviewer (strict but helpful).

# q1 answer is [1,2,3,4] and [1,2,3,4]

# ✅ Q1 — Correct.

# Let’s quickly confirm your reasoning (this is an interview favorite):

# a = [1, 2, 3]
# b = a

# Both point to the same list

# 🔹 b += [4]
# Modifies the list in-place
# So both a and b become:
# [1, 2, 3, 4]
# 🔹 b = b + [5]
# Creates a new list
# b now points somewhere else
# a remains unchanged
# ✅ Final Output:
# [1, 2, 3, 4]
# [1, 2, 3, 4]

# Good — you're understanding references now 👍

# 👉 Next (this one exposes shallow copy understanding):

# Q2:

# a = [1, 2, 3, 4]
# b = a[:]

# b.append(5)
# print(a)
# print(b)

# What’s your answer?

# a = [1]
# b = a
# print(a)
# c = a
# print(c)


# a = [2]
# b.append(3)


# c = c + [4]
# print(c)