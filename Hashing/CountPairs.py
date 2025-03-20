'''
Count such pairs
Given an array arr[] of n integers and a target value, the task is to find the number of pairs of integers in the array whose sum is equal to target.
'''

def countPairs(arr, target):
    f = dict() # Dictionary to save occurences
    count = 0 # Counter for valid pairs

    for i in range(len(arr)):
        complement = target - arr[i]
        # 1: If complement exists, add its count to count
        if complement in f:
            occurences = f[complement]
            count = count + occurences
        f[arr[i]] = f.get(arr[i], 0) + 1 
    return count

arr = list(map(int,input("Enter arr: ").split()))
target = int(input("Enter target: "))
print(countPairs(arr, target))

