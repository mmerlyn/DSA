'''
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
Given two strings s1 and s2 consisting of lowercase characters, the task is to check whether the two given strings are anagrams of each other or not.

Input: s1 = “geeks”  s2 = “kseeg”
Output: true
Input: s1 = “allergy”  s2 = “allergic”
Output: false
'''
# Using HashMap
def areAnagrams(s1, s2):
    charCount = {}
    # Count frequency of each character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
    # Count frequency of each character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
    for count in charCount.values():
        if count != 0:
            return False
    return True

s1 = "geeks"
s2 = "kseg"
# print(areAnagrams(s1, s2))

def bruteForce(s1, s2):
    m = len(s1)
    n = len(s2)
    visited = [False] * m
    count = 0
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j] and not visited[j]:
                count += 1
                visited[j] = True
    if count == m:
        return True
    else:
        return False
# print(bruteForce(s1, s2))

def prashanth(s1, s2):
    if len(s1) == len(s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
print(prashanth(s1, s2))

# Frequency Array
max = 26

def areAnagrams(s1, s2):
    freq = [0] * max

    # Count frequency of each character in s1
    for ch in s1:
        freq[ord(ch) - ord('a')] += 1
    # Count frequency of each character in s2
    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    for count in freq:
        if count != 0:
            return False
    return True




