import math
# Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order
def removeNegatives(arr):
    arr[:] = [item for item in arr if item >= 0]
    return arr
    # return arr[::-1]
sumArr = [-2,-4,0,22,993,-8]
print(removeNegatives(sumArr))
print(sumArr)

# Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.


def returnSecondToLastElement(arr):
    if (len(arr) <= 2):
        return None
    else:
        return arr[len(arr)-2]
print(returnSecondToLastElement([42,"true",4,"Kate",7]))
print(returnSecondToLastElement([42,"true",4,"Kate",7,66,"Caden",405094,"Wilcox",7]))
print(returnSecondToLastElement([42,"true",4]))
print(returnSecondToLastElement([42,"true"]))
print(returnSecondToLastElement([42]))
print(returnSecondToLastElement([]))

# Return the second-largest element of an array. Given [42,1,4,Math.PI,7], return 7. If the array is too short, return null.
# first I can keep track of the largest number by naming arr[0] the largest and iterating through the whole array once that part of the problem is done (I have the largest number) I can work backwards with a while loop to navigate through the array starting at i which will be the last index of the array then compare to see if the current num is larger than secondNum which is automatically just arr[0] and at the same time smaller than the max num to avoid making max num and secondNum the same number 

def secondLargest(arr):
    if (len(arr) <= 1):
        return None
    max = arr[0]
    secondNum = arr[0]
    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]
    while i >= 0:
        if(arr[i] > secondNum and arr[i] < max):
            secondNum = arr[i]
        i -= 1
    # print(max)
    print(secondNum)
secondLargest([422,1,4,7,77,34,23,858,-34,22])
secondLargest([34,1,4,7,77,34,23,858,-34,22])
secondLargest([34,1,4,7,77,34,23,858,344,222])
print(secondLargest([34]))
print(secondLargest([]))

# Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.
# I need to return the nth element from the arrays end so first I should traverse through the array backwords N amount of times

def nthToLast(arr, n):
    if (len(arr) <= 2):
        return arr
    i = len(arr)-1
    while n > 0:
        n-=1
        if (n != 0):
            i-=1
    return arr[i]
print(nthToLast([5,2,3,6,4,9,7], 2))
print(nthToLast([5,2,3,6,4,9,7,-33,2134,.003], 0))
print(nthToLast([5,2], 2))

# Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array). Given ([20,30,40,50,60,70],2,4), change to [20,30,70] and return it.


# givin a string return the length of the last word 
def lengthOfLastWord(str):
    newStr = str .split()
    lastWord = newStr[-1]
    print(len(lastWord))
    return newStr
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("fly me  to   the moon"))
print(lengthOfLastWord("luffy is still joyboy"))


