''' Given an Integer n, find the reverse of its digits. '''

# Using string slicing in Python

def reverseDigits(n):
    #print(n)
    # Reversing string using slicing s[start : stop : step]
    s = n[::-1]
    n = int(s)
    return n

n = input("Enter number: ")
print(reverseDigits(n))
