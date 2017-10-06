act_date = tuple(map(int,input().split()))
exp_date = tuple(map(int,input().split()))
Da = act_date[0]
Ma = act_date[1]
Ya = act_date[2]
De = exp_date[0]
Me = exp_date[1]
Ye = exp_date[2]


fine = 0
if Ya == Ye:
    if Ma == Me:
        fine = (Da-De)*15
    elif Ma < Me:
        fine = 0
    else:
        fine = (Ma-Me)*500
elif Ya < Ye:
    fine = 0
else:
    fine = 10000

print(fine)

