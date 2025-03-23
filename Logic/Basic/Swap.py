''' Given two numbers a and b, the task is to swap them. '''

# Naive Approach

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")

#Tuple Unpacking
a, b = b, a
print(f"a = {a}, b = {b}")