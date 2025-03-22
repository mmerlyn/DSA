'''
Given a string of lowercase characters from ‘a’ – ‘z’. We need to write a program to print the characters of this string in sorted order.
'''
s = "merlynmercylona"
max = 26
def sortString(s):
    count = [0] * max
    for char in s:
        count[ord(char) - ord('a')] += 1
    for i in range(max):
        for _ in range(count[i]):
            print(chr(i + ord('a')), end='')

sortString(s)
