n = int(input())
arr = list(map(int, input().split()))
arr.sort()
p = len(arr)-1
for i in range(len(arr)):
    if arr[p]== max(arr):
        p -=1
    else:
        break
print(arr[p])

