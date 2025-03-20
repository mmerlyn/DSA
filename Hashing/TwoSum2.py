'''
Check if such pair exists
Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. 
'''

def twoSum(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False

arr = list(map(int,input("Enter arr: ").split()))
target = int(input("Enter target: "))
print(twoSum(arr, target))