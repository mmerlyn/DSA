def arrayMean(arr, n):
    if n == 1:
        return arr[n - 1]
    else:
        return (arrayMean(arr, n - 1) * (n - 1) + arr[n - 1])/n
    
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(arrayMean(arr, n))