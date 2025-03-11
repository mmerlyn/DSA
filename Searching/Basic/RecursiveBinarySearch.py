# Recursive Binary Search

arr = [0, 2, 5, 6, 9, 34, 38, 45, 54, 67, 89]

def binarySearchRec(arr, low, high, key):
    if high >= low:
        mid = low + (high - low) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binarySearchRec(arr, low, mid-1, key)
        else:
            return binarySearchRec(arr, mid+1, high, key)
    else:
        return -1
    
key = int(input("Enter number to be searched: "))
print(binarySearchRec(arr, 0, len(arr)-1, key))