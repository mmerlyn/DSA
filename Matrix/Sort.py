"""
Given a m x n matrix. The problem is to sort the given matrix in strict order. 
"""

A = [[5, 4, 7], [1, 3, 8], [2, 9, 6], [21, 31, 43]]
m = len(A)
n = len(A[0])

x = []

# Copying to list
for i in range(m):
    for j in range(n):
        x.append(A[i][j])

# Sorting List
x.sort()

# Copy elements from list back to Matrix
k = 0
for i in range(m):
    for j in range(n):
        A[i][j] = x[k]
        k += 1

# Print result
res = A
for row in res:
    print(" ".join(map(str, row)))

