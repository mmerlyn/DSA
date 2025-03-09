''' In Python, list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list. 
A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations
- List can contain duplicate items
- List in Python are mutable. We can modify, replace or delete the items
- List are ordered. It maintain the order of elemets based on how they are added.
- Accessing items in list can be done directly using their index, starting from 0
- List stores references, not values: 
- The list is a container with references (addresses) to the actual values
- Python internally craetes separate objects for 10, 20, etc., then stores their memory addressed inside li
- This means that modifying an element doesn't affect other elements but can affect the referenced object if it is mutable
'''

# Creating a list
a = [1, 2, 3, 4, 5]
b = ["apple", "banana", "orange"]
c = [1, "hello", 3.14, True]
print(a)
print(b)
print(c)

# Using list constructor
d = list((1, 2, 3, 'apple', 4.5))
print(d)

# Creating list with repeated elememts
e = [2] * 5
print(e)

# Accessing list elements
print(b[0])

# Adding elements into list
b.append("blue berry")
print(b)

a.insert(0, 6)
print(a)

a.extend([7, 8 , 9, 10])
print(a)

# Updating elements in a list
a[0] = 11
print(a)

# Removing elements from list
a.remove(11)
print(a)

a.pop(8)
print(a)

del a[7]
print(a)

# Iterating over lists
for item in b:
    print(item)

# Nested List in Python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[1][1])