"""
Given a matrix mat[n][m] and an element target. return true if the target is present in the matrix, else return false
"""
def search(matrix, key):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == key:
                return True
    return False

matrix = []
rows = 3
cols = 3

print("Enter matrix: ")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

key = int(input("Enter Key: "))

print(search(matrix, key))