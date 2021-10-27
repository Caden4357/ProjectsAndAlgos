# Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order
def removeNegatives(arr):
    arr[:] = [item for item in arr if item >= 0]
    return arr
    # return arr[::-1]
print(removeNegatives([-2,-4,0,22,993,-8]))

# Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.

def returnSecondToLastElement(arr):
    return arr[len(arr)-2]
print(returnSecondToLastElement([42,"true",4,"Kate",7]))