#!/usr/bin/python3
'''
Defines class Rectangle that inherits class Base
'''
class Rectangle(Base):
    '''
    Class Rectangle with private instance attributes
    __width -> width

    __height -> height

    __x -> x

    __y -> y
    each with its own public getter and setter.
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):

    Call the super class with id - this super call with use the logic of the __init__ of the Base class

    Assign each argument width, height, x and y to the right attribute.
    '''
    @property
    def width(self):
        '''
        Gets width
        '''
        return self.__width
    @width.setter
    def width(self, width):
        '''
        Sets width
        '''
        self.__width = width
    @property
    def height(self):
        '''
        Gets height
        '''
        return self.__height
    @height.setter
    def height(self, height):
        '''
        Sets height
        '''
        self.__height = height
    @property
    def x(self):
        '''
        Gets x
        '''
        return self.__x
    @x.setter
    def x(self, x):
        '''
        Sets x
        '''
        self.__x = x
    @property
    def y(self):
        '''
        Gets y
        '''
        return self.__y
    @y.setter
    def y(self, y):
        '''
        Sets y
        '''
        self.__y = y
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Class constructor for class Rectangle
        '''
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
