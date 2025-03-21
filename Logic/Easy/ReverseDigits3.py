''' Given an Integer n, find the reverse of its digits. '''

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

n = input("Enter a number: ")
print(reverseDigits(n))