''' Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on. '''
# Using Temporary array

def reverseArray(arr):
    n = len(arr)
    temp = [0] * n

    for i in range(n):
        temp[i] = arr[n - i - 1]

    for i in range(n):
        arr[i] = temp[i]
    return arr

arr = list(map(int, input("Enter array numbers: ").split()))
print(reverseArray(arr))