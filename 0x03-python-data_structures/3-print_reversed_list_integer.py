#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Julius Okeyo <jaykopiyo@gmail.com>

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    length = len(my_list)

    for i in range(length, 0):
        print("{}".format(my_list[i]))
