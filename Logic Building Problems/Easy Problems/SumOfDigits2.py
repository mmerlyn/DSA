''' Given a number n, find the sum of its digits. '''
# Recursive Approach

'''The idea is to extract the last digit. add it to the sum, and recursively call the function 
with the remaining number (after removing the last digit)'''

def sum_of_digits(n):
    # base case
    if n == 0:
        return 0
    # recursive case
    return n % 10 + sum_of_digits( n // 10 )

n = int(input("Enter n: "))
print(sum_of_digits(n))
