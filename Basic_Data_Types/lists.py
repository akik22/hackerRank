#!/usr/bin/python3

populated_list = []

for _ in range(int(input())):

    command, *values = input().split()
    values = list(map(int,values))

    if command == 'insert':
        populated_list.insert(values[0],values[1])
    elif command == 'print':
        print(populated_list)
    elif command == 'remove':
        populated_list.remove(values[0])
    elif command == 'append':
        populated_list.append(values[0])
    elif command == 'sort':
        populated_list.sort()
    elif command == 'pop':
        populated_list.pop()
    elif command == 'reverse':
        populated_list.reverse()


# Alternate Solution

populated_list = []

for _ in range(int(input())):

    given_input = input().split()

    if hasattr(populated_list,given_input[0]):
        getattr(populated_list,given_input[0])(*map(int,given_input[1:]))
    else:
        print(populated_list)















