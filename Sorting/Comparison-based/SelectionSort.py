''' Selection Sort: 
Selection sort is a comparison-based algorithm. 
First we find the smallest element and swap it with the first element. This way, we get the smallest element at the correct position
Then we find the smallest among the remaining elements and swap it with the second element.
We keep doing this until we get all elements move to the correct position
'''

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        min_inx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_inx]:
                min_inx = j
        arr[i], arr[min_inx] = arr[min_inx], arr[i]
    return arr
            
arr = list(map(int, input("Enter array: ").split()))
print(selectionSort(arr))