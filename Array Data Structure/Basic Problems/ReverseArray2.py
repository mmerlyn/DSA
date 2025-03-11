''' Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on. '''

''' Two Pointer Approach - The idea is to maintain two pointers: left and right, such that left points at the beginning of the array and right points to the end of the array. 
While left pointer is less than the right pointer, swap the elements at these two positions. After each swap, increment the left pointer and decrement the right pointer to move towards the center of array. This will swap all the elements in the first half with their corresponding element in the second half.'''

def reverseArray(arr):
    left = 0
    right = len(arr) -1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = list(map(int, input("Enter array numbers: ").split()))
print(reverseArray(arr))