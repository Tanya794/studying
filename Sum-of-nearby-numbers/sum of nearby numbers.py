# sum of nearby numbers is a new element inserted between these numbers

from random import *

lst = [randint(1,9) for k in range(8)]
print(lst)
p = 1
k = 0
for i in range(len(lst) - 1):
    
    s = lst[i + k] + lst[p]
    lst.insert(p, s)
    p += 2
    k += 1
print(lst)
