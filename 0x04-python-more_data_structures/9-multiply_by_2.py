#!/usr/bin/python3
# 9-multiply_by_2.py
# Julius Okeyo <jaykopiyo@gmail.com>

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary.keys():
        new_dictionary[key] = 2 * a_dictionary[key]
    return (new_dictionary)
