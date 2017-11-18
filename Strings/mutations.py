#!/usr/bin/python3

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string

# Another Approach:

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

