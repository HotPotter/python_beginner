'''
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ') # rpartition(sep) returns a 3-tuple that contains the part before the separator, the separator and the part after the separator
    d[item] = d.get(item, 0) + int(quantity) #get() returns a value of the given key
for item, quantity in d.items():
    print(item, quantity)
'''

d = {}
for _ in range(int(input())):
    item, quantity = input().rsplit(' ',maxsplit=1)
    d[item] = d.get(item,0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)