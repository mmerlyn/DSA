''' Given a string of lowercase characters from ‘a’ – ‘z’. 
We need to write a program to print the characters of this string in sorted order. 
'''

''' Efficient Approach: 
There will be a total of 26 unique characters only
We can store the count occurrences of all the characters from a to z in a hashed array
The 1st index of the hashed array will represent a, 2nd b and so on
Finally, we will simply traverse the hashed array and print the characters from a to z the number of times they occured in input string
'''
max = 26
def sortString(s):
    count = [0] * max

    # Traverse the string, count the characters and store the frequency in 'count' hash array
    # ord(ch) -> ASCII value of char | ord('a') -> ASCII value of a = 97
    # ord(ch) - ord('a') -> Gives 0 - 25 positions for each char
    for ch in s:
        count[ord(ch) - ord('a')] += 1
    
    # Traverse the count array
    for i in range(max):
        # As many times as the frequency for each char
        for j in range(count[i]):
            # (i + ord('a')) -> calculates ASCII value of char | chr() converts it back to the char
            print(chr(i + ord('a')), end = '')

s = input("Enter string: ")
sortString(s)
