"""
Given two m x n matrices m1 and m2, the task is to subtract m2 from m1 and return res.
"""

def subtract(A, B):
    m = len(A)
    n = len(A[0])
    C = [[0] * n] * m
    if len(B) != m or len(B[0]) != n:
        print("Invalid Input")
    else:
        for i in range(m):
            for j in range(m):
                C[i][j] = A[i][j] - B[i][j]
        return C
    
A = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
B = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

res = subtract(A, B)
for row in res:
    print(' '. join(map(str, row)))