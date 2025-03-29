""" 
Given two N x M matrices. Find a N x M matrix as the sum of given matrices each value at the sum of values of corresponding elements of the given two matrices. 
"""

def add(A, B):
    m = len(A)
    n = len(A[0])
    C = [[0] * n] * m
    if len(B) != m or len(B[0]) != n:
        print("Invalid")
    else:
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
        return C

A = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
B = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

res = add(A, B)

for row in res:
    print(' '.join(map(str, row)))