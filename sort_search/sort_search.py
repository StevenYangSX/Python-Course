##TODO: review all the search and sort algorithms

'''Linear Search'''
'''Linear search is the basic search algorithm used in data structures. 
It is also called as sequential search. Linear search is used to find a 
particular element in an array.'''

arr = [14,7,3,54,23,8,9]

def linearSearch(arr, target):
    index = 0
    for index in range(0,len(arr)):
        if(arr[index] == target):
            return index
        
    return -1

#function call
result = linearSearch(arr, 54)
#print(result)


'''Binary Search'''
''' 1. input must be sorted
    2. devide input to 2 sub array
    3. compair the target with mid value and see if target lie
       in the first part or the second part.
    4. iteraton / recursive calls for sub arrays until get the 
       target'''

sortedArr = sorted(arr)
print(sortedArr)
#mid = len(sortedArr) // 2




#TODO: sort algorithms
'''Selection Sort: find min in the given array, put it in a new array.
    then, keep finding the min in input array and append it to the resule 
    array. until finish'''

toBeSorted = [24,46,31,64,1,532,33,687,21,-21]
print(toBeSorted)
def findMin(arr):
    temp = arr[0]
    for i in range(len(arr)):
        if(temp >= arr[i]):
            temp = arr[i]
    return temp

def selectionSort(arr):
    arrayCopy = toBeSorted
    print(arrayCopy)
    min_value = arrayCopy[0]
    result = []
    while(len(arrayCopy) != 0):
        temp = findMin(arrayCopy)
        arrayCopy.remove(temp)
        result.append(temp)
    return print(result)
    
#selectionSort(toBeSorted)


'''Bubble Sort: Bubble Sort is the simplest sorting algorithm that
 works by repeatedly swapping the adjacent elements if they are in 
 wrong order. Means::  compair 1st with 2nd then 2nd vs. 3rd and then
 keep going. keep swapping and finally get the right order'''

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return print(arr)


#bubbleSort(toBeSorted)

