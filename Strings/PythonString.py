s = "GeeksforGeeks"

res = []
for i in range(len(s)-1, -1, -1):
    res.append(s[i])
print(''.join(res))