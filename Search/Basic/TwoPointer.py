''' Given a sorted array arr (sorted in ascending order) and a target, find if there exists any pair of elements (arr[i], arr[j]) such that their sum is equal to the target. '''

''' Two Pointer Technique: begin with two corners of the given array. We use two index variables left and right to traverse from both corners.
Initialize: left = 0, right = n – 1
Run a loop while left < right, do the following inside the loop

Compute current sum, sum = arr[left] + arr[right]
If the sum equals the target, we’ve found the pair.
If the sum is less than the target, move the left pointer to the right to increase the sum.
If the sum is greater than the target, move the right pointer to the left to decrease the sum.
'''

arr = [-8, 1, 4, 6, 10, 45]

def twoSum(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        sum = arr[left] + arr[right]

        if target == sum:
            return True
        elif target < sum:
            right = right - 1
        else:
            left = left + 1
    return False

target = int(input("Enter the target sum: "))
print(twoSum(arr, target))