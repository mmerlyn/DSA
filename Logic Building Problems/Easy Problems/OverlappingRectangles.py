''' Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates. 
l1: Top Left coordinate of first rectangle. 
r1: Bottom Right coordinate of first rectangle. 
l2: Top Left coordinate of second rectangle. 
r2: Bottom Right coordinate of second rectangle. '''

# Ex: l1 = (0, 10) r1 = (10, 0) l2 = (5, 5) r2 = (15, 0) | Overlap
# Ex: l1 = (0, 10) r1 = (10, 0) l2 = (-10, 5) r2 = (-1, 0) | Don't overlap

# Appraoch: 
# 2 Rectangles do not overlap if either of these conditions is true
# 1) One rectangle is above top edge of other rectangle
# 2) One rectangle is on left side or left edge of other rectangle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def isOverlap(l1, r1, l2, r2):
    # side by side overlap
    if r1.x < l2.x or r2.x < l1.x:
        return True
    
    # vertical overlap
    if r1.y < l2.y or r2.y < l1.y:
        return True
    return False

def get_point(name):
    x, y = map(int, input(f"Enter coordinates for {name} (x y): ").split())
    return Point(x, y)

print("Enter coordinates for the first rectangle: ")
l1 = get_point("Top-Left (l1)")
r1 = get_point("Bottom-Right (r1)")

print("Enter coordinates for the second rectangle: ")
l2 = get_point("Top-Left (l2)")
r2 = get_point("Bottom-Right (r2)")

if isOverlap(l1, r1, l2, r2):
    print("Rectangles overlap.")
else:
    print("Rectangles do not overlap.")