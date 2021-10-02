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

# Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
# change the array to [3,1,2]. Don't use built-in functions.
# Second: allow negative shiftBy (shift L, not R).
# Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
# Fourth: minimize the touches of each element.












# Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

def filterRange(arr, min, max):
    for i in range(len(arr)-1):
        if(arr[i] < min):
            arr.pop(i)
        elif(arr[i] > max):
            arr.pop(i)
    return arr
print(filterRange([5,4,2,6,18,901,900,899.99], 1, 900))


# Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].

def concat(arr1, arr2):
    arr3 = arr1 + arr2
    return arr3
print(concat(['a', 'b'], [1,2]))