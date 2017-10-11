for _ in range(int(input())):
    value = input().split()
    print(value[0],*value[1] if len(value)> 1 else 'a')