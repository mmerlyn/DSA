'''
Given an array arr[] of integers and a number x, the task is to find the smallest subarray with a sum strictly greater than x.
'''
def smallestSubWithSum(arr, x):
    n = len(arr)
    min_len = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum = current_sum + arr[end]
        while current_sum > x:
            min_len = min(min_len, end-start+1)
            current_sum = current_sum - arr[start]
            start += 1
    return min_len if min_len != float('inf') else 0

arr = list(map(int, input("Enter array elements: ").split()))
x = int(input("Enter number x: "))
print(smallestSubWithSum(arr, x))