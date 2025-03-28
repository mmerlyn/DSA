""" Given an array arr[] of size n, the task is to reverse the array using Stack. """

def reverseArray(arr):
    st = []
    for i in range(len(arr)):
        st.append(arr[i])
    i = 0
    while (len(st) > 0):
        top = st.pop()
        arr[i] = top
        i += 1
    return arr
arr = list(map(int, input('Enter array: ').split()))
print(reverseArray(arr))
