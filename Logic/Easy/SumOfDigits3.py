''' Given a number n, find the sum of its digits. '''

# Taking Input number as a String

'''The idea is to take the input number as a string and then iterate over all the characters (digits) 
to find the sum of digits. To find the actual value of a digit from a character, 
subtract the ASCII value of ‘0’ from the character. This approach is used when 
the input number is so large that it cannot be stored in integer data types.

The 'ord' function in python returns unicode point of a given character
ord('0') = 48 | ord('3') = 51 | 3 = ord('3') - ord('0')
This is a common trick to convert character digits into actual integers without using int()'''

def sum_of_digits(s):
    sum = 0
    for i in range(len(s)):
        digit = ord(s[i]) - ord('0')
        sum += digit
    return sum

s = input("Enter a number: ")
print(sum_of_digits(s))