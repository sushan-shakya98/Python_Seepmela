# Dictionaries
# boy = {
#         'Name': 'Ali',
#         'Age': 21,
#         'Height': 6,
#         'Weight': 68,
#         'City':'Peshawar',
#         'Religion': 'Muslim'
#     }
# print(boy)
# {
#     'Name': 'Ali',
#     'Age': 21,
#     'Height': 6,
#     'Weight': 68,
#     'City':'Peshawar',
#     'Religion': 'Muslim'
# }

# a = {
#     "Name" : "Hari",
#     "Address" : "Boudha",
#     "Age" : 27,
#     "Phone" : 123456,
#     "List1" : [123, 456],
#     "Address" : "Kathmandu"
# }
# print(type(a))
# print(a["Name"]) // while accessing use mainly keys like key1 or otherwise use Address
# print(a["Phone"])
# print(len(a))
# print(a["Address"]) // output kathmandu becuz it shows the last assign value
# polymorphism ??


#  // 
# a = {
#     "Name" : "Hari",
#     "Address" : "Boudha",
#     "Age" : 27,
#     "Phone" : 123456,
#     "List1" : [123, 456],
#     "Address" : "Kathmandu"
# }
# print(a.keys()) // shows keys names
# print(a.values()) // shows valued pairs

# a["Name"] = "Sabin"
# print(a)

# print(a["List1"][1]) //accessing list1 second value output => 456

# user_info = {
#     "name" : "sushan",
#     "age" : 27
# }
# user_info['name'] = "Hari"
# user_info['age'] = 30
# user_info['phone'] = 123
# print(user_info)

# update the value
# user_info.update({
#     "name" : "Hari",
#     "age" : 123,
#     "phone" : 123,
#     "role" : "teacher"
# })
# print(user_info)

# boy = {
#     'Name': 'Ali',
#     'Age': 21,
#     'Height': 6,
#     'Weight': 68,
#     'City': 'Islamabad',
#     'Religion': 'Muslim'
#     }


# del boy['Age']
# print(boy)

# boy.pop('Religion') //.pop() shows pop expected give 1 argument
# print(boy)

# boy.popitem()
# print(boy)

# boy.clear()
# print(boy)


# practice
# user_info = {
#     "name" : "Hari",
#     "age" : 123,
#     "phone" : [
#         {
#             "type" : "NTC",
#             "number" : 9844
#         },
#         {
#             "type" : "Ncell",
#             "number" : 980
#         },
#         {
#             "type" : "Jio",
#             "number" : 9742
#         },

#     ],
#     "role" : "teacher"
# }
#  output hari Ntc number is 9844
# output hari ncell number is 980

# output = f'{user_info['name']} {user_info['phone'][0]['type']} number is {user_info['phone'][0]['number']} '
# output1 = f'{user_info['name']} {user_info['phone'][1]['type']} number is {user_info['phone'][1]['number']} '
# print(output)
# print(output1)
# print(f'{user_info['name']} {user_info['phone'][0]['type']} number is {user_info['phone'][2]['number']}')


# user_info = {
#     "name" : "Hari",
#     "address" : {
#         "temp": "dang",
#         "per" : "Imadol"
#     }
# }
# print(user_info["address"]["per"])
# # or
# address = user_info['address']
# print(address['per'])

