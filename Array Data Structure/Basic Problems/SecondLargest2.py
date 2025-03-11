''' Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array. If the second largest element does not exist, return -1. '''

''' Two Pass Approach - We traverse the array twice. In the 1st traversal, we find the maximum element
In the second traversal, find the maximum element ignoring the one we found in the 1st traversal'''

def SecondLargest(arr):
    n = len(arr)
    largest = 0
    for i in range(0, n):
        if arr[i] > largest:
            largest = arr[i]

    second_largest = 0
    for i in range(0, n):
        if arr[i] != largest and arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest

arr = list(map(int, input("Enter array elements: ").split()))
print(SecondLargest(arr))
