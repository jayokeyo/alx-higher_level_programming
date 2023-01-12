#!/usr/bin/python3
# 8-simple_delete.py
# Julius Okeyo <jaykopiyo@gmail.com>

def simple_delete(a_dictionary, key=""):
    del a_dictionary[key] if key is in a_dictionary
    return (a_dictionary)
