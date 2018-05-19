'''
Created on May 18, 2018

@author: Linden Holt
'''
import random
import math

def merge (arr, leftStart, rightEnd):
    #initialize counters and indicies for main sorting algorithm
    temp = [None]*10
    leftEnd = ((leftStart + rightEnd)//2)
    rightStart = leftEnd+1
    l = leftStart
    r = rightStart
    index = leftStart
    
    #main sorting algorithm sorts values from split arrays into a temporary array
    while l <= leftEnd and r <= rightEnd:
        if arr[l] <= arr[r]:
            temp[index] = arr[l]
            l += 1
        else:
            temp[index] = arr[r]
            r += 1
        index += 1    
        
    #while loops to copy remaining values from the left or right partitions into the temp array
    while l <= leftEnd:
        temp[index] = arr[l]
        index += 1
        l += 1
        
    while r <= rightEnd:
        temp[index] = arr[r]
        index += 1
        r += 1
        
    # Copy sorted elements from temp back into arr
    for i in range(leftStart, rightEnd+1):
        arr[i] = temp[i];
         
    return[arr]

def mergeSort (arr, leftStart, rightEnd):
    if leftStart < rightEnd:
        middle = (leftStart+(rightEnd))//2
        mergeSort(arr, leftStart, middle)
        mergeSort(arr, middle+1, rightEnd)
        merge (arr, leftStart, rightEnd)
    
    return arr

#populates array with random integers, calls Mergesort function


arr = []
for i in range(10):
    arr.append(random.randint(1,100))

print(arr)
n = len(arr)
print(mergeSort(arr, 0, n-1))