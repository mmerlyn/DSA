''' You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube. '''

# Naive Approach

def dice(n):
    if n == 1:
        print(6)
    elif n == 2:
        print(5)
    elif n == 3:
        print(4)
    elif n == 4:
        print(3)
    elif n == 5:
        print(2)
    else:
        print(1)

n = int(input("Enter number on the face of the cube: "))
dice(n)