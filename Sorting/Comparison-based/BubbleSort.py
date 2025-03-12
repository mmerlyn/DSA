'''Bubble Sort
We sort the array using multiple passes. After the first pass, the maximum element goes to end (its correct position). Same way, after second pass, the second largest element goes to second last position and so on.
In every pass, we process only those elements that have already not moved to correct position. After k passes, the largest k elements must have been moved to the last k positions.
'''

def bubbleSort(arr):
    n = len(arr)
    # Each Pass
    for i in range(n):
        swapped = False
        # Last i elements are in correct place, traverse through remaning n-i
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # At the end of each pass, if swapped == False, it means the array is already sorted
        # So the program terminates early using break thus optimized algorithm by preventing unnecessary passes
        if (swapped == False):
            break
    return arr

arr = list(map(int, input("Enter array: ").split()))
print(bubbleSort(arr))