''' Rotations in the array is defined as the process of rearranging the elements in an array by shifting each element to a new position. This is mostly done by rotating the elements of the array clockwise or counterclockwise. '''

''' Reversal Algorithm - if we right rotate the array by d positions, the last d elements will be in the front and first (n – d) elements will be at the end. 
First reverse all the elements of the array. 
Then reverse first d elements.
Finally, reverse last (n – d) elements to get the final rotated array.
'''

def rotateArray(arr, d):
    n = len(arr)
    d = d % n
    # Reverse entire array
    arr.reverse()

    # Reverse the first d elements
    arr[:d] = reversed(arr[:d])

    # Reverse remaining n - d elements
    arr[d:] = reversed(arr[d:])
    return arr

arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter by how many times do you want to rotate: "))
print(rotateArray(arr, d))