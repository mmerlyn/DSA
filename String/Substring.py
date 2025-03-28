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

def isSubsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    i, j = 0, 0
    while (i < m and j < n):
        if (s1[i] == s2[j]):
            i += 1
        else:
            i = 0
        j += 1

    return i == m

txt = "geeksforgeeks"
pat = "eks"
idx = txt.find(pat)
print(idx)
