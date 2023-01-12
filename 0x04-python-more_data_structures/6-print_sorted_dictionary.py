#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Julius Okeyo <jaykopiyo@gmail.com>

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
