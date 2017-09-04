n = int(input())
pb = {}
for i in range(0,n):
    entry = input().split()
    pb[entry[0]]=int(entry[1])

while True:
    q = input()
    try:
        pb[q]
        print(q,"=",pb[q],sep="")
    except:
        print("Not found")
