""" Given a sentence, we need to print the reverse of individual words. """

def reverseWords(str):
    st = []
    res = ""
    for ch in str:
        if ch != " ":
            st.append(ch)
        else:
            while st:
                res += st.pop()
            res += " "
    # last word
    while st:
        res += st.pop()
    return res
str = input("Enter sentence: ")
print(reverseWords(str))
        