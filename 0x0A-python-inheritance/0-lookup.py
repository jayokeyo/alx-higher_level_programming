#!/usr/bin/python3
# 0-lookup.py
# Julius Okeyo <jaykopiyo@gmail.com>
'''
methods and attributes lookup function
'''
def lookup(obj):
    '''
    Defines method for returning all defined
    objects in a class
    '''
    return (dir(obj))
