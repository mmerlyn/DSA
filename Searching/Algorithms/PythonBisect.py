''' Bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.
Python has in-built bisect algorithms in the bisect module which allows keeping the list sorted after the insertion of each element.
This is essential as this reduces overhead time required to sort the list again and again after the insertion of each element
'''

''' bisect(list, num, beg, end): returns the position in the sorted list where the number passed in argument can be placed so as to manintain the resultant list sorted.
If the element is already present in the list, the rightmost position where the element has to be inserted is returned

bisect_right(list, num, beg, end): does the same as above.

bisect_left(list, num, beg, end): does the same as above but if the element is already present in the list, the leftmost position where the element has to be inserted is returned

insort(list, num, beg, end): Works same as bisect(list, num, beg, end) but returns the sorted list instead of the index to be inserted

insort_right(list, num, beg, end): Works same as above

insort_left(list, num, beg, end): Works same as bisect_left(list, num, beg, end), but but returns the sorted list instead of the index to be inserted
'''

import bisect

li = [1, 3, 5, 5, 5, 9, 11, 13]

num = int(input("Enter a number to be inserted: "))

print(bisect.bisect(li, num))
print(bisect.bisect_right(li, num))
print(bisect.bisect_left(li, num))

li2 = [12, 14, 15, 15, 17, 18, 19, 20]
bisect.insort(li2, num)
print(li2)
# bisect.insort_right(li2, num)
# bisect.insort_left(li2, num)

