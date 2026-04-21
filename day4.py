# print("Hello")
# print("Sushan")

# list1 = [1,2,2,3,5,4,6]
# list2 = ["Red", "Green", "Blue"]
# print(list1)
# print(list1[5])
# print(list2)
# print(list2[1])
# print(type(list2))
# print(len(list1))
# print(len(list1)-1)

# list3 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
#print(type(list3[len(list3)-1]))
# print(isinstance(list3[len(list3)-1], float))
# print(isinstance(list3[7], float))

#teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
# print(teachers[0:4])
# print(teachers[ :5])
# print(teachers[4: ])
# print(teachers[2:4])
# print(teachers[1:1])
# print(teachers[0:1])

#append
# teachers.append("Sushan")
# print(teachers)
#teachers.append("Sushan","Sabin") // this will display error cuz it take only one value

#insert
# teachers.insert(2,"Messi")
# print(teachers)

#extend
# language = ["Nepali", "Englis", "Chinese"]
# language.extend(['Japanese', 'Spanish'])
# print(language)

a = [1,2,3,4,5,6]
b = [7,8]
# print(a.extend(b))
# print(b.extend(a))
# print(a)
# print(b)

#Concatenate
# language = ["Nepali", "English", "Chinese"]
# country = ["Nepal", "USA"]
# student = language + country
# print(student)

#del
#fruits = ["apple", "mango", "banana", "grapes"]
#del fruits[2]
#del fruits["apple"] // this will throw error cuz it follows indexing number
#print(fruits)

#remove = only one first mango
# fruits = ["apple", "mango", "banana", "grapes", "mango"]
# fruits.remove("mango")
# print(fruits)


#pop removes the last index list
# fruits.pop()
# print(fruits)


#clear => all the elements from the list
# fruits = ["apple", "mango", "banana", "grapes"]
# fruits.clear()
# print(fruits)

# count =>  method returns the number of elements/item with the specified value(itemname)
# teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
# count_teacher = teachers.count('Haris')
# print(count_teacher)

# index => index() method returns the position/index at the first occurrence of the specified value(itemname)
# teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
# index_teacher = teachers.index('Irfan')
# print(index_teacher)

#sort => Sort the list alphabetically
# teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
# teachers.sort()
# print(teachers)

# NESTED LIST
# b = [6, 7, 8, 9]
# a = [1, 2, 3, 4, 5, [6, 7, 8, 9], b]

# print(a)

# c = [1, 2, 3, 4, 5, [6, 7, 8, 9]]
# print(c[5][2])
# print(c[-1][-2])
# d = c[-1]
# print(d[2])

# d = [1, 2, 3, [4, 5], [6, 7], [(8)]]
# output = [1, 2, 3, 4, 5, 6, 7, 8] using isinstance and extend

