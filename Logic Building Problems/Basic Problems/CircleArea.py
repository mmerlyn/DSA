''' Given the radius r. Find the area of a circle. The area of the circle should be correct up to 5 decimal places. '''

# Formula: PI * r * r

import math

def circle_area(r):
    return math.pi * r * r

r = int(input("Enter radius: "))
print(round(circle_area(r), 2))