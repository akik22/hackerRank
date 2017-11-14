#!/usr/bin/python3

student_info = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    student_info.append([name,score])


student_info = sorted(student_info, key= lambda key: (key[1],key[0]))

for student in student_info:
    if student_info[0][1] != student[1]:
        second_highest = student[1]
        for student in student_info:
            if second_highest == student[1]:
                print(student[0])
        break


# Some slight Modification:

student_info = [[input(),float(input())] for _ in range(int(input()))]

student_info = sorted(student_info, key= lambda key: (key[1],key[0]))

for student in student_info:
    if student_info[0][1] != student[1]:
        second_highest = student[1]
        for student in student_info:
            if second_highest == student[1]:
                print(student[0])
        break