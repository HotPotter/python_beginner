class Calculator(object):
    """docstring for Calculator."""

    def power(self, n,p):
        if n >= 0 and p >= 0:
            result = n**p
            return result
        else:
            return "n and p should be non-negative"

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
