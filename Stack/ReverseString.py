""" Given a string str, the task is to reverse it using stack.  """

def reverseString(s):
    # Push all characters onto the stack
    s = list(s)

    # Pop characters to form revered string
    res = " "
    
    while s:
        res += s.pop()
    return res

str = input("Enter string: ")
print(reverseString(str))