#Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.
# [1,2,3,4,5] 6 
# [6,1,2,3,4,5]

# the quick way to push to front the challenge is to not use built ins I feel like this qualifies as a built in but I like it and think it will come in handy later so I'm throwing it in
def pushToFront(arr, val):
    newArr = [val, * arr]
    return newArr
print(pushToFront([5,4,3,2,1], 6))
print(pushToFront([200,18,15,4,3,2,1], 6))

# Using a while loop seems to be the best way to go about this in python using a for loop I kept getting index out of bounds errors 
def pushToFront2(arr, val):
    arr = arr + [1]
    temp1 = arr[0]
    temp2 = arr[1]
    i = 0
    while i < len(arr):
        try:
            arr[i+1] = temp1
            temp1 = temp2
            temp2 = arr[i+2]
            i+=1
        except IndexError:
            arr[0]=val
            return arr
print(pushToFront2([200,18,15,4,3,2,1], 6))

# Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().
def popFront(arr):
    removedItem = arr.pop(0)
    return removedItem
print(popFront([1,2,3,5,4]))