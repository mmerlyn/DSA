# Iterative Binary Search

arr = [0, 2, 5, 6, 9, 34, 38, 45, 54, 67, 89]

def binarySearch(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2 # To avoid floor values
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
        
key = int(input("Enter key to be searched: "))
result = binarySearch(arr, 0, len(arr) - 1, key)
print(result)