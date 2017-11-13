#!/usr/bin/python3

given_input = int(input())

if given_input%2:
    print("Weird")
elif given_input>=2 and given_input<5:
    print("Not Weird")
elif given_input >= 6 and given_input<=20:
    print("Weird")
else:
    print("Not Weird")