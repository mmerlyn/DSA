''' You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube. '''

# Using sum of 2 sides
# The idea is based on the observation that the sum of 2 opposite sides of a cubical dice = 7
# So just subtract the given n from 7 and print the answer

def dice(n):
    ans = 7 - n
    return ans

n = int(input("Enter number on the face of the cube: "))
print(dice(n))