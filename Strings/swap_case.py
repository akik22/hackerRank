#!/usr/bin/python3

def swap_case(string_input):

    modified_sentence_list = []

    for character in string_input:
        if character.isupper():
            modified_sentence_list.append(character.lower())
        else:
            modified_sentence_list.append(character.upper())

    modified_sentence = ''.join(modified_sentence_list)

    return modified_sentence

# Alternate Approach:

def swap_case(string_input):
    return string_input.swapcase()