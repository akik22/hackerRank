#!/usr/bin/python3

number_of_element_in_tuple= int(input())
element_of_tuple = tuple(map(int,input().split()))

print(hash(element_of_tuple))