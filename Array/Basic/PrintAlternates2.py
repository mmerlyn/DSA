''' Given an array arr[], the task is to print every alternate element of the array starting from the first element. '''

# Recursive Approach

def getAlternatesRec(arr, index, res):
    if index < len(arr):
        res.append(arr[index])
        getAlternatesRec(arr, index + 2, res)

def getAlternates(arr):
    res = []
    getAlternatesRec(arr, 0, res)
    return res

arr = list(map(int, input("Enter array numbers: ").split()))
print(getAlternates(arr))