import collections
li=[]
for _ in range(int(input())):
    li.append(input())
c = collections.Counter(li)
print(len(c))
print(*c.values())


'''
for python 3.5 and before
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

li=[]
for _ in range(int(input())):
    li.append(input())
c = OrderedCounter(li)
num_k = 0
num_v = []
for k,v in c.items():
    num_k += 1
    num_v.append(v)
print(num_k)
print(' '.join(map(str,num_v)))

'''

'''
for python 3.5 and before
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
'''