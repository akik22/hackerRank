#!/usr/bin/python3

x = int(input())
y = int(input())
z = int(input())
N = int(input())

# Breakdown:

poplulated_list = []


for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != N:
                poplulated_list.append([i,j,k])

print(poplulated_list)

# By list comprehension:

poplulated_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != N]

print(poplulated_list)