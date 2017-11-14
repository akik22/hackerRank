#!/usr/bin/python3

number_of_integers = int(input())
integers = sorted(list(map(int,input().split())), reverse=True)

for i in integers:
    if integers[0] != i:
        print(i)
        break

# Alternate Approach:

number_of_integers = int(input())

# Set used to remove the duplicates:

integers = set(map(int,input().split()))
integers = sorted(list(integers))

print(integers[-2])