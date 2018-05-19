'''
Created on May 19, 2018

@author: gamebox
'''
import random
import math

def partition (arr, left, right, pivot):
    while left <= right:
        
        while arr[left] < pivot:
            left += 1
        
        while arr[right] > pivot:
            right -= 1
        
        if (left <= right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    
    return left

def quickSort(arr, left, right):
    if (left < right):
        
        pivot = arr[(left+right)//2]
        middle = partition(arr, left, right, pivot)
        quickSort(arr, left, middle-1)
        quickSort(arr, middle, right)
    
    return arr
        
arr = []
for i in range(10):
    arr.append(random.randint(1,100))

print(arr)
n = len(arr)
print(quickSort(arr, 0, n-1))