def binary_search(array, element):
    mid = 0
    start = 0
    end = len(array) 
    step = 0
    
    while (start <= end):
        print("Subarray in step {}:{}".format(step,str(array[start:end+1])))
        step += 1
        mid = (start + end)//2
        
        if element == array[mid]:
            return mid
        
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return - 1

array = [1,2,3,4,5,6,7,8,9,10]

element = 7

print("Searching for {} in {}".format(element, array))
print("Index of {}:{}".format(element, binary_search(array, element)))
