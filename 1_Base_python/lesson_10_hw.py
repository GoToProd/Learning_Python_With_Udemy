#Решение к 1 заданию
array = [154,161,167,170,171,174,176,182]
def average(array):
    temp = 0
    temp1 = set(array)
    count = len(temp1)
    for i in temp1:
        temp+=i
        res = temp/count
    return res
print (average(array))

#Более простой вариант
second_array = sum(array)
third_array = len(array)
result = (second_array / third_array)
print (result)

#Решение к 2 заданию
array2 = ["UK", "China", "USA", "France", "New Zealand", "UK", "France"]
# n = int(input())
# arr = set()
# for i in range(n):
#     arr.add(input())
# print(len(arr))
array2_res = set(array2)
print (len(array2_res))



# #Решение к 3 заданию
# a = int(input())
# for i in range(a):
#     b = set(input().split())
# c = int(input())
# for i in range(c):
#     d = set(input().split())
# res = b.symmetric_difference(d)
# print(len(res))

array3 = [1,2,3,4,5,6,7,8,9]
array4 = [1,2,3,6,8,10,11,12,13]
set3 = set(array3)  
set4 = set(array4)  

non_matching = set3.symmetric_difference(set4)  
coming = set3.intersection(set4)
mass_sets = set3.union(set4)
count = len(non_matching)  
count2 = len(coming)
count3 = len(mass_sets)

print(f'Количество разных: {count}, а вот сами числа {non_matching}')
print(f'Количество общих: {count2}, а вот сами числа {coming}')
print(f'Какое то количство общего всего полученного оператором union {count3} и сами числа {mass_sets}')


# #Решение к 4 заданию
# a = int(input())
# c = set(input().split())
# b = int(input()) 
# d = set(input().split())

# res = c.difference(d)
# print(len(res))

# #Решение к 5 заданию
# a = int(input())
# arr= set(input().split())
# c = int(input())
# arr1 = set(input().split())
# res = arr1.intersection(arr)
# print(len(res))


# #Решение к 6 заданию

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# a = int(input())
# b = set(input().split())
# c = int(input())
# d = set(input().split())
# res = b.union(d)
# print(len(res))

