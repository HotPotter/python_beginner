import sys


arr = [
[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0],
]

a = arr
all_sums = []
for row_idx in range(len(a)-2):
    for col_idx in range(len(a[0])-2):
        hour_glass = []
        hour_glass += a[row_idx][col_idx:col_idx+3]
        hour_glass += [a[row_idx+1][col_idx+1]]
        hour_glass += a[row_idx+2][col_idx:col_idx+3]
        print(hour_glass)
        all_sums.append(sum(hour_glass))

print(max(all_sums))
