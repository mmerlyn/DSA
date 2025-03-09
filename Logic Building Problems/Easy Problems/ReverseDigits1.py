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
    
