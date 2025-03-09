''' Given two numbers a and b, the task is to swap them. '''

# Python built-in swap

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"a = {a}, b = {b}")

#Tuple Unpacking
a, b = b, a
print(f"a = {a}, b = {b}")