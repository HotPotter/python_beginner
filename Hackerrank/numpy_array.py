import numpy
def arrays(arr):
    return numpy.array(list(reversed(arr)),float)
arr = input().split(' ')
result = arrays(arr)
print(result)
