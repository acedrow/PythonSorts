'''
Created on May 19, 2018

@author: gamebox
'''

def mergeSort (leftStart, rightEnd):
    if leftStart < rightEnd:
        middle = (leftStart+(rightEnd))//2
        print("ls: ", leftStart, "re: ", rightEnd, "middle: ", middle)
        mergeSort(leftStart, middle)
        mergeSort(middle+1, rightEnd)

leftStart = 0
rightEnd = 9   
mergeSort(leftStart, rightEnd)