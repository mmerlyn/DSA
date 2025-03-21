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