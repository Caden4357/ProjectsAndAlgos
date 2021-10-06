# Given an array of comparable values, move the lowest element to array’s front, shifting backward any elements previously ahead of it. Do not otherwise change the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. As always, do this without using built-in functions.

#1.) return null for invalid inputs 
# 2.) find the smallest element and the index of the smallest element 
# 3.) shift backwards any elements previous to smallest element 

def minToFront(arr):
    if len(arr) <= 1:
        return arr
    min = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    while index >= 0:
        arr[index] = arr[index-1]
        index -=1
    arr[0] = min
    return arr
print(minToFront([1,2,-3,-4,7,6,11]))
print(minToFront([1]))
print(minToFront([]))