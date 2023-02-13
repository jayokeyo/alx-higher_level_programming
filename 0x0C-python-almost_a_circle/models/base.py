#!/usr/bin/python3
'''
Defines class base
'''
class Base:
    '''
    Class Base with private class attribute __nb_objects, and
    def __init__(self, id=None):
    '''
    __nb_objects = 0

    def __init__(self, id = None):
        '''
        Defines class constructor __init__
        '''
        if (id is not None):
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
