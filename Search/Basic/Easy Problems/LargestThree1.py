''' Given an array arr[], the task is to find the top three largest distinct integers present in the array. 
If there are less than three distinct elements in the array, then return the available distinct numbers in descending order.
'''
# Effective Solution - 1 Traversal

def largestThree(arr):
    n = len(arr)

    if n < 3:
        print("Invalid Input")
        return

    largest = second_largest = third_largest = float('-inf')

    for i in range(n):
        if arr[i] > largest:
            third_largest = second_largest
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            third_largest = second_largest
            second_largest = arr[i]
        elif arr[i] < second_largest and arr[i] > third_largest:
            third_largest = arr[i]
    return largest, second_largest, third_largest

arr = list(map(int, input("Enter the array elements: ").split()))
print(largestThree(arr))