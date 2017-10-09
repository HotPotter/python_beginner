from collections import deque
def op_deq(arg, n):
    for _ in range(n):
        value = input().split(' ')
        getattr(arg, value[0])(*value[1] if len(value)>1 else [])
    return arg
n = int(input())
d = deque()
result = op_deq(d,n)
print(*result)