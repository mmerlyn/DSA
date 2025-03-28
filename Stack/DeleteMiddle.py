""" Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure. """

def deleteMiddle(st):
    temp_st = []
    n = len(st)
    mid = n // 2
    for _ in range(mid):
        temp_st.append(st.pop())
    middle_e = st.pop()
    while temp_st:
        st.append(temp_st.pop())
    return middle_e, st

st = list(map(int, input("Enter elements: ").split()))
print(deleteMiddle(st))