"""
Given a sorted matrix mat[][] of size nxm and an element x, the task is to find if x is present in the matrix or not. 
Matrix is sorted in a way such that all elements in a row are sorted in increasing order and for row i, where 1 <= i <= n-1, 
the first element of row i is greater than or equal to the last element of row i-1.
"""

def searchMatrix(A, key):
    m = len(A)
    n = len(A[0])

    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2

        mid_row = mid // n
        mid_col = mid % n

        if A[mid_row][mid_col] == key:
            return True      
        if A[mid_row][mid_col] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

A = [[1, 2], [3, 4], [5, 6]]
key = int(input("Enter key: "))

print(searchMatrix(A, key))
