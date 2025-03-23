'''
A pangram is a sentence containing all letters of the English Alphabet.
Given a string s, the task is to check if it is Pangram or not. 

Input: s = “The quick brown fox jumps over the lazy dog” 
Output: true
'''

max = 26

def checkPanagram(s):
    visited = [False] * max
    for i in range(len(s)):
        # Uppercase Character
        if 'A' <= s[i] <= 'Z':
            visited[ord(s[i]) - ord('A')] = True
        elif 'a' <= s[i] <= 'z':
            visited[ord(s[i]) - ord('a')] = True
    for i in range(max):
        if not visited[i]:
            return False
    return True

s1 = "The quick brown fox jumps over the lazy dog"
s2 = "The quick brown fox jumps over the dog"

print(checkPanagram(s1))
print(checkPanagram(s2))

