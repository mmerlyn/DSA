'''Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn’t exist '''

arr = [14, 2, 4, 6, 15, 8, 10, 12, 17]

def linearSearch(arr, e):
    for i in range(len(arr)):
        if arr[i] == e:
            return i
    return -1

e = int(input("Enter element to be searched: "))
print(linearSearch(arr, e))