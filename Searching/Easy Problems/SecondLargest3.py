''' Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array. If the second largest element does not exist, return -1. '''

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

arr = list(map(int, input("Enter array elements: ").split()))
print(secondLargest(arr))
