''' Given an array arr[], the task is to print every alternate element of the array starting from the first element. '''

# Iterative Approach

def getAlternates(arr):
    res = []
    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res

arr = list(map(int, input("Enter arr numbers: ").split()))
print(getAlternates(arr))

# Recursive Approach

def getAlternatesRec(arr, index, res):
    if index < len(arr):
        res.append(arr[index])
        getAlternatesRec(arr, index + 2, res)

def getAlternates(arr):
    res = []
    getAlternatesRec(arr, 0, res)
    return res