from collections import Counter

num_shoes = int(input())
shoes = Counter(map(int,input().split()))
num_cust = int(input())

earn = 0

for i in range(num_cust):
    size, price = map(int, input().split())
    if size in shoes and shoes[size]>0:
        earn += price
        shoes[size] -= 1

print(earn)