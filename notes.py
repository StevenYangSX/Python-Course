#####       Binary Search  ########
def binarySearch(L, secret=73):
    '''
    L must be sorted.
    '''
    left = 0
    right = len(L) -1
    while left <= right:
        mid = (left+right)/2
        if L[mid] == secret:
            return mid
        elif L[mid] < secret:
            left = mid + 1
        else:
            right = mid -1
    return -1
#######################################################
'''Selection Sort'''
#TODO: Recall how seleciton sort works!!

def findMinIndex(inList, start):
    return


def selectionSort (inList):
    for i in range(len(inList)):
        # find min value index 
        min_index = findMinIndex(inList, i)  # TODO
        # swap L[i] and L[min_index]
        #inList[i] inList[min_index] = inList[min_index] inList[i]
#TODO run and test
#######################################################
'''Bubble Sort'''
#TODO: Recall....

def bubbleSort(L):
    L = [1, 3, 2,4,0]
#   len = 5
    for j in range(len(L)):
        for i in range(len(L) - 1 -j):
            if L[i] > L[i+1]:
                #swap
               # L[i] L[i+1] = L[i+1] L[i]
#return 

#######################################################

def testFun ():
    pring("This is testing")


testFun()