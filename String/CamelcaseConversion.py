'''
Given a sentence having lowercase characters, the task is to convert it to Camel Case.
In Camel Case, words are joined without spaces, the first word keeps its original case, and each subsequent word starts with an uppercase letter.
'''

def camelcaseConverison(s):
    res = []
    capitalizeNext = False
    for i in range(len(s)):
        # If we encounter a space, set the flag to capitaliza
        if s[i] == ' ':
            capitalizeNext = True
        # If the flag is set, capitalize the current character
        elif capitalizeNext:
            res.append(s[i].upper())
            capitalizeNext = False
        # Or else just add the character to the list
        else:
            res.append(s[i])
    return ''.join(res)

s = input("Enter lowercase string: ")
print(camelcaseConverison(s))