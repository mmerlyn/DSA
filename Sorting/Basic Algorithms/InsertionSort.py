''' 
We start with second element of the array as first element in the array is assumed to be sorted.
Compare second element with the first element and check if the second element is smaller then swap them.
Move to the third element and compare it with the first two elements and put at its correct position
Repeat until the entire array is sorted
'''

def insertionSort(arr):
    n = len(arr)
    # Start from 2nd element, assume 1st element to be sorted
    for i in range(1, n):
        # key - The number to be inserted
        key = arr[i]
        # j - To track the position where key should be inserted
        j = i - 1

        # Move the elements that are greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in the correct position
        arr[j + 1] = key
    return arr

arr = list(map(int, input("Enter array: ").split()))
print(insertionSort(arr))