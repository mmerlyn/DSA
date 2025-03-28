""" Given an array arr[] of integers, the task is to find the Next Greater Element 
for each element of the array in order of their appearance in the array.
Note: The Next Greater Element for an element x is the first greater element on the 
right side of x in the array. Elements for which no greater element exist, 
consider the next greater element as -1.  

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]

Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
"""

def nextLarger(arr):
    n = len(arr)
    res = [-1] * n
    st = []

    for i in range(n-1, -1, -1):
        # Pop all elements smaller than or equal to current
        while st and st[-1] <= arr[i]:
            st.pop()
        # If stack is not empty, then top is next greater
        if st:
            res[i] = st[-1]
        # Push current element to stack
        st.append(arr[i])
    return res
        
arr = list(map(int, input("Enter array numbers: ").split()))
print(nextLarger(arr))

