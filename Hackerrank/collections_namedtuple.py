
from collections import namedtuple
num_stu = int(input())
Student = namedtuple('Student',input())
total = 0
for _ in range(num_stu):
    li = input().split()
    students= Student(*li)
    total += int(students.MARKS)

print(total/num_stu)

