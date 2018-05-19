'''
Created on May 17, 2018

@author: Linden Holt
'''
import random
#bubblesort function definition

def bubbleSort (arr):
    while True:
        swap = False;
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True
        if swap == False:
            break
        
    
    return arr

#populates array with random integers, calls bubblesort function

arr = []
for i in range(10):
    arr.append(random.randint(1,100))

print(arr)
print(bubbleSort(arr))


    