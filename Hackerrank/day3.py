import sys


N = int(input().strip())
def numCheck (N):
    if N % 2 > 0 : return "Weird"
    if N % 2 == 0:
        if N < 5 : return "Not Weird"
        if N <= 20: return "Weird"
        if N > 20: return "Not Weird"

print(numCheck(N))
