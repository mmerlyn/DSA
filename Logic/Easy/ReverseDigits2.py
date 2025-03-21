''' Given an Integer n, find the reverse of its digits. '''

# Using Recursion

def reverseDigits(n, rev):
    if n == 0:
        return rev  
    rev = rev * 10 + (n % 10)
    return reverseDigits(n // 10, rev)

n = int(input("Enter a number: "))
print(reverseDigits(n, 0))
        


