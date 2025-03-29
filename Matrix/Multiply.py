""" 
Given two matrices, the task is to multiply them. Matrices can either be square or rectangular:
The #columns in Matrix-1 must be equal to the #rows in Matrix-2
"""
def multiply(A, B):
    r1 = len(A)
    r2 = len(B)
    c1 = len(A[0])
    c2 = len(B[0])

    if c1 != r2:
        print("Invlaid Input!")
        return None
    
    res = [[0] * c2] * r1

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] = A[i][k] * B[k][j]
    return res

A = [[1, 2], [3, 4], [5, 6]]
B = [[1, 2, 3], [4, 5, 6]]

res = multiply(A, B)
for row in res:
    print(" ".join(map(str, row)))