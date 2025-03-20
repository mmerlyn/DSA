''' Quick Sort Algorithm - QuickSort works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

There are mainly three steps in the algorithm:

Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
'''

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = list(map(int, input("Enter unsorted array: ").split()))
n = len(arr)
quickSort(arr, 0, n - 1)

for val in arr:
    print(val, end=" ")