'''
Check if such pair exists
Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. 
'''

def twoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
    return False

arr = list(map(int, input("Enter a: ").split()))
target = int(input("Enter target sum: "))
print(twoSum(arr, target)) 

# Check if such pair exists

def twoSum(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False