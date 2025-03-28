s = []
s.append(10)
s.append(20)
s.append(30)

print(f"{s[-1]} popped from stack")
s.pop()

print(f"Top element is: {s[-1]}")
print("Elements present in stack: ")

while s:
    print(s.pop())