""" Given a string str, the task is to reverse it using stack.  """

def reverseString(s):
    s = list(s)
    res = " "
    while s:
        res += s.pop()
    return res
s = input("Enter String: ")
print(reverseString(s))