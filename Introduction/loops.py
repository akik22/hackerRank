#!/usr/bin/python3

given_number = int(input())

for square in range(given_number):
    print(square**2)


# Alternate Solution:

given_number = int(input())

print(*[square**2 for square in range(given_number)], sep='\n')
