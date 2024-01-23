# print('----------------------------------------------------------------')


# users = {'Tom', 'Bob', 'Alice', 'John'}
# users2 = users.copy()
# print(users2)

# users = {'Tom', 'Bob', 'Alice', 'John'}
# users2 = {'Alan', 'Bebur', 'Angy', 'Simon'}
# print(users.union(users2))

# users = {'Tom', 'Bob', 'Alice', 'John'}
# users2 = {'Tom', 'Kate', 'Alice', 'Tony'}
# print(users.intersection(users2))

# users = {'Tom', 'Bob', 'Alice', 'John'}
# users2 = {'Tom', 'Kate', 'Alice', 'Tony'}
# print(users.difference(users2))
# print(users2.difference(users))

# users = {'Tom', 'Bob', 'Alice', 'John'}
# users2 = {'Tom', 'Kate', 'Alice', 'Tony'}
# print(users.isdisjoint(users2))


# def to_set(element):
#     st = set(element)
#     return st, len(st)

# print(to_set('Hello World'))


# def diff(set1, set2, set3, symmetric = True):
#     if symmetric:
#         return set1 ^ set2 ^ set3
#     return set1 - set2 - set3

# set1 = {1, 2 , 3}
# set2 = {1, 2, 6}
# set3 = {1, 2, 4}

# print(diff(set1, set2, set3))


# def superset(set1, set2):
#     if set1 > set2:
#         print(f'Objects {set1} is superset')
#     elif set1 == set2:
#         print(f'Objects {set1} and {set2} is equal')
#     elif set1 < set2:
#         print(f'Objects {set2} is superset')
#     else:
#         print('Superset is not find')

# set1 = {1, 8 , 5 ,3}
# set2 = {3,5}
# set3 = {5,3,8,1}
# set4 = {90,100}

# superset(set1, set2)
# superset(set1, set3)
# superset(set2, set3)
# superset(set4, set2)

def set_gen(lst):
    index = 0 
    while index < len(lst):
        cnt = (lst.count(lst[index]))
        if cnt > 1:
            lst[index] = str(lst[index]) * cnt
        index += 1
    return set(lst)

print(set_gen([2,2,1,2,2,5,6,7,1,3,2,2])) 