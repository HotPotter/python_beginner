import sys

arr = [
[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0],
]

sum_all = []
for m in range(4):
    for r in range(4):
        sub_arr = [arr[m][r:r+3],arr[m+1][r+1:r+2],arr[m+2][r:r+3]]
        print(sub_arr)
        total = 0
        for i in sub_arr:
            total = total + sum(i)
        sum_all.append(total)
print(max(sum_all))

'''
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
'''
# first sub_arr
'''
sub_arr = [arr[0][0:3],arr[1][0:3],arr[2][0:3]]
total = 0
for i in sub_arr:
    total = total + sum(i)
print(total)
'''
