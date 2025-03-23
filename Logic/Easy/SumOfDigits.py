''' Given a number n, find the sum of its digits. '''
# Iterative Approach

'''The idea is to add the digits starting from the rightmost (least significant)
digit and moving towards the leftmost (most significant) digit. 
This can be done by repeatedly extracting the last digit from the number using modulo 10 operation, 
adding it to the sum, and then removing it using integer division by 10.'''

# For eg: n = 1567, then 1567 / 10 = 156.7 = 156(Integer Division).

def sum_of_digits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum

n = int(input("Enter n: "))
print(sum_of_digits(n))

# Recursive Approach

'''The idea is to extract the last digit. add it to the sum, and recursively call the function 
with the remaining number (after removing the last digit)'''

def sum_of_digits(n):
    # base case
    if n == 0:
        return 0
    # recursive case
    return n % 10 + sum_of_digits( n // 10 )

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