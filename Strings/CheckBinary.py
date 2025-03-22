'''
Given a string s, the task is to check if it is a binary string or not. A binary string is a string which only contains the characters '0' and '1'.
'''

def isBinary(s):
    for i in range(len(s)):
        if s[i] != '0' and s[i] != '1':
            return False
    return True

s = input("Enter String: ")
print(isBinary(s))