import sys
from itertools import combinations as comb


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    # brutal force solutuion
    '''
    combs = [c for c in comb(range(1,n+1),2)]
    alist =[]
    for c in combs:
        if c[0]&c[1] < k:
            alist.append(c[0]&c[1])
    print(max(alist))
'''
    print(k - 1 if ((k - 1) | k) <= n else k - 2)



