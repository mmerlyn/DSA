''' Rotations in the array is defined as the process of rearranging the elements in an array by shifting each element to a new position. This is mostly done by rotating the elements of the array clockwise or counterclockwise. '''

''' Rotate one by one - At each iteration, shift the elements by one position to the right in a circular fashion (the last element becomes the first). Perform this operation d times to rotate the elements to the right by d positions.'''

def rotateArray(arr, d):
    n = len(arr)
    for i in range(d):
        last = arr[n - 1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]  
        arr[0] = last
    return arr

arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter by how many times do you want to rotate: "))
print(rotateArray(arr, d))