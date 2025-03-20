'''Merge Sort - Merge sort is a popular sorting algorithm known for its efficiency and stability. 
It follows the divide-and-conquer approach to sort a given array of elements.
Divide:  Divide the list or array recursively into two halves until it can no more be divided. 
Conquer:  Each subarray is sorted individually using the merge sort algorithm. 
Merge:  The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged. 
'''

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid 

    # Temporary Arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary array
    for i in range(n1):
        L[i] = arr[low + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = j = 0
    k = low

    # Merge the temp arrays back into array
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)

def printArr(arr):
    for i in arr:
        print(i)

arr = list(map(int, input("Enter array: ").split()))
mergeSort(arr, 0, len(arr) - 1)
print(arr)