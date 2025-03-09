# You are given two coordinates (x1, y1) and (x2, y2) of a two-dimensional graph. Find the distance between them.
# (x1, y1) = (3, 4) (x2, y2) = (7, 7) | O/P: 5
# (x1, y1) = (3, 4) (x2, y2) = (4, 3) | O/P: 1.41421
# Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)

import math
def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

x1, y1 = map(int, input("Enter x1, y1: ").split())
x2, y2 = map(int, input("Enter x2, y2: ").split())

print(distance(x1, y1, x2, y2))