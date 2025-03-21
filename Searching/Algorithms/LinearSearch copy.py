''' Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn’t exist. '''

arr = [10, 12, 15, 17, 8, 9, 9, 9, 21]

def LinearSearch(arr, e):
    for i in range(0, len(arr)):
        if arr[i] == e:
            return i
    return -1

e = int(input("Enter number to search: "))
print(LinearSearch(arr, e))