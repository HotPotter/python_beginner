class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        diff=[]
        b = 0
        for num in a:
            for i in range(a.index(num)+1, len(a)):
                b = abs(num - a[i])
                diff.append(b)

        self.maximumDifference = max(diff)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
