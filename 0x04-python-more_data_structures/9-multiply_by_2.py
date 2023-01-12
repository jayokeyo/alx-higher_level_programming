#!/usr/bin/python3
# 9-multiply_by_2.py
# Julius Okeyo <jaykopiyo@gmail.com>

def multiply_by_2(a_dictionary):
    for key in a_dictionary.keys():
        a_dictionary[key] = 2 * a_dictionary[key]
    return (a_dictionary)
