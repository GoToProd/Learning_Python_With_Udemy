users = {1:"Dias", 
         2:"Martes", 
         3:"Mikola", 
         4:"Jue"}
# emails = {1:"dias@example.com", 2:"Martesv@example.com", 3:"Mikola@example.com", 4:"Jue@example.com"}

# obj = {}
# obj1 = dict()

# user_list = [
#     ['+123456', 'Tom'],
#     ['+1234567', 'Jerry'],
#     ['+1234568', 'Dias'],
#     ['+12345678', 'Martes'],
#     ['+1234569', 'Mikola'],
#     ['+123456789', 'Jue'],
# ]

# user_dict = dict(user_list)

# print (user_dict)
# print (user_list)


# print(users[1])
# users[1] = 'Jish'
# print(users[1])


key = 2
user = users.pop(key)
#print(user)

#users.clear()
#print(users)

for key in users:
    print(f'Index: {key} User: {users[key]}')
