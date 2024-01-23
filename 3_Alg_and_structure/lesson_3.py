# def bubbleSort(x):
#     n = len(x)
    
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if x[j]>x[j+1]:
#                 x[j],x[j+1] = x[j+1],x[j]
            
# x = [64, 2, 22, 14, 876, 233, 673, 234, 152]

# print(bubbleSort(x))
# for i in range(len(x)):
#     print(x[i])

# def selectionSort(x):
#     n = len(x)
#     for i in range(n):
#         min_id = i
#         for j in range(i+1, n):
#             if (x[j] < x[min_id]):
#                 min_id = j
#             x[i], x[min_id] = x[min_id], x[i]
#     return x
    
# x = [64, 2, 35, 77, 1, 57, 99, 93, 21]
# # x = [64, 2, 22, 14, 876, 233, 673, 234, 152]
# print(selectionSort(x))
# for i in range(len(x)):
#     print(x[i])

# def insersionSort(x):
#     n = len(x)
#     for i in range(1, n):
#         key = x[i]
#         j = i - 1
#         while x[j] > key and j >= 0:
#             x[j+1] = x[j]
#             j -= 1
#             x[j+1] = key
#     return x
        
# x = [64, 2, 35, 77, 1, 57, 99, 93, 21]
# # x = [64, 2, 22, 14, 876, 233, 673, 234, 152]
# print(insersionSort(x))
# for i in range(len(x)):
#     print(x[i])


# def quickSort(x):
#     n = len(x)
#     if n > 1:
#         pivot = x.pop()
#         grt_lst = []
#         eql_lst = [pivot]
#         sml_lst = []
#         for i in x:
#             if i == pivot:
#                 eql_lst.append(i)
#             elif i > pivot:
#                 grt_lst.append(i)
#             else:
#                 sml_lst.append(i)
#         return (quickSort(sml_lst) + eql_lst + quickSort(grt_lst))
#     else:
#         return x
    
# x = [64, 2, 22, 14, 876, 233, 673, 234, 152]
# print(quickSort(x))   


def mergeSort(x):
    n = len(x)
    if n == 1: return x
    mid = int(len(x)/2)
    lst1 = mergeSort(x[:mid])
    lst2 = mergeSort(x[mid:])
    result = merge(lst1, lst2)
    return result

def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i < len(lst1) and j < len(lst2)):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j += 1
    while(j < len(lst2)):
        lst.append(lst2[j])
        j += 1
    while(i < len(lst1)):
        lst.append(lst1[i])
        i += 1
    return lst

x = [64, 2, 22, 14, 876, 233, 673, 234, 152]
print(mergeSort(x))  