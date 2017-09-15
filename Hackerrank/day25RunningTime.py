#pirnt runtime
import time
start_time = time.time()

#long runtime version
# T = int(input())
# for i in range (T):
#     num = int(input())
#     for f in range(2,num):
#         if num%f == 0:
#             result = "Not prime"
#             break
#         else:
#             result = "Prime"
#     print(result)


#short runtime version
# import math
# T = int(input())
# for i in range (T):
#     num = int(input())
#     sqt = int(math.sqrt(num))
#     for f in range (2,sqt+1):
#         if num % f == 0:
#             result=("Not prime")
#             break
#         else:
#             result=("Prime")
#
#     print(result)

#even shorter runtime version
import math
def check_prime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

T = int(input())
for i in range (T):
    num = int(input())
    print(check_prime(num))







print("--- %s seconds ---" % (time.time() - start_time))