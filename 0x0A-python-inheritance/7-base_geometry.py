#!/usr/bin/python3
'''
Defines class BaseGeometry
'''

class BaseGeometry:
    '''
    class BaseGeometry with public methods area and integer_validator
    '''

    def area(self):
        '''
        Area function
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Integer validator function.
        Args:
            name: name of integer
            value: value of integer
        '''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (value < 0):
            raise ValueError("{} must be greater than 0".format(value))
