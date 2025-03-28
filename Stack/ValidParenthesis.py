""" Given a string s representing an expression containing various types of brackets: {}, (), and [], the task is to determine whether the brackets in the expression are balanced or not. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order. """

def validParenthesis(s):
    st = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            st.append(s[i])
        elif st and ((st[-1] == "(" and s[i] == ")") or
                     (st[-1] == "[" and s[i] == "]") or
                     (st[-1] == "{" and s[i] == "}")):
            st.pop()
        else:
            return False
    return not st

str = input("Enter: ")
print(validParenthesis(str))