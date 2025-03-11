''' Rotations in the array is defined as the process of rearranging the elements in an array by shifting each element to a new position. This is mostly done by rotating the elements of the array clockwise or counterclockwise. '''

''' Using Temporary Array - Use a temporary array of size n, where n is the length of the original array. If we right rotate the array by d positions, the last d elements will be in the beginning and the first (n – d) elements will be at the end. '''

def rotateArray(arr, d):
    n = len(arr)

    # Handle case when d > n
    d = d % n

    temp = [0] * n

    # Copy last d elements to the beginning of temp
    for i in range(d):
        temp[i] = arr[n - d + i]

    # Copy first (n - d) elements to the end of temp
    for i in range(n - d):
        temp[d + i] = arr[i]
    
    for i in range(n):
        arr[i] = temp[i]
    return arr
    
arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter by how many times do you want to rotate: "))
print(rotateArray(arr, d))