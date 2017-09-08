import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
'''
    r = 1
    while n > 0:
        r = r*n
        n = n-1
    return r
'''

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
