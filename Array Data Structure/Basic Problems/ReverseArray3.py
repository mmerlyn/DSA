''' Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on. '''

''' Swapping - The idea is to iterate over the first half of the array and swap each element with its corresponding element from the end. So, while iterating over the first half, any element at index i is swapped with the element at index (n – i – 1). '''

def reverseArray(arr):
    n = len(arr)
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
    return arr

arr = list(map(int, input("Enter array numbers: ").split()))
print(reverseArray(arr))