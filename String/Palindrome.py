'''
Given a string s, the task is to check if it is palindrome or not.
'''

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = input("Enter string: ")
print(isPalindrome(s))