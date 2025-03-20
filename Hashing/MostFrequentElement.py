'''
Given an array, find the most frequent element in it. If there are multiple elements that appear a maximum number of times, print any one of them.
'''

def mostFrequent(arr, n):
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1

    max_count = 0
    res = -1
    for element in Hash:
        if (Hash[element] > max_count):
            res = element
            max_count = Hash[element]
    return res, max_count

arr = list(map(int, input("Enter arr: ").split()))
n = len(arr)
print(mostFrequent(arr, n))

                