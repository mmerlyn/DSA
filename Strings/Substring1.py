'''
Given a string s, the task is to check if it is palindrome or not.
'''
def findSubstring(txt, pat):
    n = len(txt)
    m = len(pat)
    for i in range(n-m+1):
        j = 0
        while j < m and txt[i+j] == pat[j]:
            j += 1
        if j == m:
            return i
    return -1

txt = "geeksforgeeks"
pat = "eks"
print(findSubstring(txt, pat))