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

#Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).
[4,3,2,5,6], 2, 8
[4,3,2,5,6,0]
[4,3,8,2,5,6]

def insertAt(arr, idx, val):
    if(idx > len(arr)-1):
        return arr
    elif(len(arr) < 2):
        return arr
    else:
        arr = arr + [0]
        i = 0
        while i < len(arr):
            try:
                if(i == idx):
                    temp1 = arr[i]
                    arr[i] = val
                    temp2 = arr[i+1]
                    i+=1
                    while i < len(arr):
                        arr[i] = temp1
                        temp1 = temp2
                        temp2 = arr[i+1]
                        i+=1
                    return arr
                else:
                    arr[i] = arr[i]
                    i+=1
            except IndexError:
                return arr
print(insertAt([5,4,6,4,8], 0, 2))
print(insertAt([33,4,-334,0,2,99,100,34,3,22,90,0,.99,.0934], 10, .8))
print(insertAt([], 0, 2))
print(insertAt([2], 10, 266))
print(insertAt([2,6,5,55,499,22,3,-99], 10, 266))

# Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
#array – move values within the array that you are given. As always, do not use built-in array functions such as splice().

def reverseWithoutBuiltIns(arr):
    length = len(arr)
    for i in range(int(length/2)):
        n = arr[i]
        arr[i] = arr[length - i - 1]
        arr[length - i - 1] = n
    return arr
print(reverseWithoutBuiltIns([5,4,3,2,1,0,9,-88,22,-0.4]))

