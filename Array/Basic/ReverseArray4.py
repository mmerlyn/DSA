''' Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on. '''

''' Recursion - Use recursion and define a recursive function that takes a range of array elements as input and reverses it. Inside the recursive function, 
Swap the first and last element. 
Recursively call the function with the remaining subarray. '''

def reverseArrayRec(arr, l, r):
    if l >= r:
        return
   
    arr[l], arr[r] = arr[r], arr[l]
    reverseArrayRec(arr, l + 1, r - 1)

def reverseArray(arr):
    n = len(arr)
    reverseArrayRec(arr, 0, n - 1)
    return arr
    
arr = list(map(int, input("Enter array numbers: ").split()))
print(reverseArray(arr))