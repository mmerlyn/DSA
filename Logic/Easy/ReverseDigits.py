''' Given an Integer n, find the reverse of its digits. '''

# I/P: 12345 O/P: 54321

'''Reversing digit by digit - This approach reverses the digits of a given number n. It works by repeatedly extracting the 
last digit of n using the modulus operator (n % 10) and appending it to the reverse number (revNum). 
After extracting the digit, the number n is reduced by integer division by 10
This process continues until n becomes 0. Finally, the reversed number (revNum) is returned.'''

n = int(input("Enter a number: "))
rev = 0

while( n != 0 ):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)

# Using Recursion

def reverseDigits(n, rev):
    if n == 0:
        return rev  
    rev = rev * 10 + (n % 10)
    return reverseDigits(n // 10, rev)

# Converting to String

'''The approach reverses a number by converting it into a string, reversing the string, 
and then converting it back into an integer. This avoids manual digit manipulation by string operations. 
The string reversal is done using a built-in function, and the result is then converted back to an integer and returned. 
This method is straightforward but requires extra space for the string conversion.'''

def reverseDigits(n):
    s = list(n)
    s.reverse()
    # To join a sequence of characters or strings into a single string
    s = ''.join(s)
    n = int(s)
    return n

# Using string slicing in Python

def reverseDigits(n):
    #print(n)
    # Reversing string using slicing s[start : stop : step]
    s = n[::-1]
    n = int(s)
    return n
    
