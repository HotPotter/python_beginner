import sys
''' number to base
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]
'''
n = int(input().strip())

def decToBin (n):
    digits = str()
    while n>0:
        digits = digits + str(n % 2)
        n = n//2
    return digits[::-1]

m = decToBin(n)
#print(m)
lst = m.split("0")
#print(lst)
print(max([len(s) for s in lst]))
