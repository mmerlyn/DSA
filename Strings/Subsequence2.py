'''
A subsequence is a sequence that can be derived from another sequence by deleting some elements 
without changing the order of the remaining elements. 
Given two strings s1 and s2, find if the first string is a Subsequence of the second string, 
i.e. if s1 is a subsequence of s2. 
Recursive Approach:
'''
def isSubsequence(s1, s2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
    if s1[m-1] == s2[n-1]:
        return isSubsequence(s1, s2, m-1, n-1)
    return isSubsequence(s1, s2, m, n-1)

s1 = "gksrek"
s2 = "geeksforgeeks"
m = len(s1)
n = len(s2)
print(isSubsequence(s1, s2, m, n))