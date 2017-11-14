#!/usr/bin/python3

student_info = dict()

for _ in range(int(input())):
    name, *number = input().split()
    number = tuple(map(float,number))
    student_info[name]=number

student_query = student_info[input()]
print('{:.2f}'.format(sum(student_query)/len(student_query)))