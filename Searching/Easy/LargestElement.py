''' Given an array arr. The task is to find the largest element in the given array '''

arr = [0, -1, -2, -13, -15]
def largestElement(arr):
    largest = 0
    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

print(largestElement(arr))
