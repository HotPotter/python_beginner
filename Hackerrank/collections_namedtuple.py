
from collections import namedtuple
num_stu = int(input())
Student = namedtuple('Student',input())
total = 0
for _ in range(num_stu):
    value1,value2,value3,value4 = input().split()
    students= Student(value1,value2,value3,value4)
    total += int(students.MARKS)

print(total/num_stu)

