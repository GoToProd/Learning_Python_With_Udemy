number = [1,2,3,4,5]
name = ['Tom', 'Jerry', 'Jim']
number1 = []
#number2 = list[]

objects = ['Person',True,1,2,3,4,5,6]

#print(number)
#print(name)
#print(objects)

# number2=[5]*6
# print(number2)

# name = ['Tom', 'Bob'] * 6
# print(name)

# print(name[0])
# print(name[1])
# print(name[2])
# print()
# print(name[-1])
# print(name[-2])
# print(name[-3])

# name[1] = 'Josh'
# print(name)

# i = 0
# while i < len(name):
#     print(name[i])
#     i+=1

# for i in range(len(name)):
#     print(name[i])


name = ['Tom', 'Bob', 'Sam']

# name.append('Alice')
# print(name)

# name.insert(2, 'Josh')
# print(name)

# name.extend(['Andrew', 'Jim'])
# print(name)

# index_start = name.index('Jim')
# print(index_start)

# removed_id = name.pop()
# print(removed_id)

# name.remove('Alice')
# print(name)

# name.clear()
# print(name)

del_name = 'Bob'
if del_name in name:
    name.remove("Tom")
    print(del_name + " is removed from the list")
else:
    print(del_name + " is not in the list")