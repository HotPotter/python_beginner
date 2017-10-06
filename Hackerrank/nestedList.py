all_list = []
for i in range(int(input())):
    name = input()
    score = float(input())
    all_list.append([str(name), score])

all_list.sort()
score_list=[i[1]for i in all_list]
p = 1
for t in range(len(all_list)):
    if  all_list[p][1] == sorted(list(set(score_list)))[1]:
        print(all_list[p][0])
        p+=1
    else:
        break


#not finished yet

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

