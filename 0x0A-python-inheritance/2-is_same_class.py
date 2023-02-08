#!/usr/bin/python3
# 2-is_same_class.py
# Julius Okeyo <jaykopiyo@gmail.com>
'''
Defines a function that validates whether
an object belongs to a particular class
'''
def is_same_class(obj, a_class):
    '''
    Checks if obj belongs to a_class.
    Args:
        obj: object to be tested.
        a_class: class it should belong to.
    '''
    return type(obj) is a_class
