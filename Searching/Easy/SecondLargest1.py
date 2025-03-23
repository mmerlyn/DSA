''' Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array. If the second largest element does not exist, return -1. '''

# Naive Approach - sort, and compare the second last element with last element

def secondLargest(arr):
    arr.sort()
    n = len(arr)

    if arr[n-2] != arr[n-1] and arr[n-2] < arr[n-1]:
        return arr[n-2]
    return -1

arr = list(map(int, input("Enter the list elements: ").split()))
print(secondLargest(arr))

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

''' One Pass Approach - The idea is to keep track of the largest and second largest element while traversing the array. Initialize largest and secondLargest with -1. '''

def secondLargest(arr):
    largest = -1
    second_largest = -1
    for i in range(0, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest

