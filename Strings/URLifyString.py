'''
Write a method to replace all the spaces in a string with ‘%20’. 
You may assume that the string has sufficient space at the end 
to hold the additional characters and that you are given the “true” length of the string.

Input: "Mr John Smith", 13
Output: Mr%20John%20Smith
Input: "Mr John Smith   ", 13
Output: Mr%20John%20Smith
'''

s = input("Enter String: ")

# Trim the given string
s = s.strip()

# Replace all spaces with %20
s = s.replace(' ', "%20")
print(s)

def replaceSpaces(s):
    rep = "%20"
    for i in range(len(s)):
        if (s[i] == ' '):
            s = s.replace(s[i], rep)
    print(s)

replaceSpaces(s)