'''
A subsequence is a sequence that can be derived from another sequence by deleting some elements 
without changing the order of the remaining elements. 
Given two strings s1 and s2, find if the first string is a Subsequence of the second string, 
i.e. if s1 is a subsequence of s2. 
Iterative Approach:
'''

def isSubsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    i, j = 0, 0
    while (i < m and j < n):
        if (s1[i] == s2[j]):
            i += 1
        j += 1
    return i == m

s1 = "gksreki"
s2 = "geeksforgeeks"
print(isSubsequence(s1, s2))
