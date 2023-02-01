#!/usr/bin/python3
# 0-rectangle.py
# Julius Okeyo <jaykopiyo@gmail.com>
'''
Class Rectangle
'''

class Rectangle:
    '''
    Class Rectangle with class attributes width and height
    '''
    def __init__(self, width = 0, height = 0):
        '''
        Initializing instance of class Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''

        self.width = width
        self.height = height
    
    def __str__(self):
        '''
        Overwrites the builtin __str__ method
        '''

        string = ""

        if self.height == 0 or self.width == 0:
            return string
        for i in range(self.height):
            string += (self.width * "#")
            if i + 1 is not self.height:
                string += "\n"
        return string
    def __repr__(self):
        """
        Overwrites the builtin __repr__ method
        """

        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")
    @property
    def width(self):
        '''
        Method width for retrieving width
        '''

        return self.__width
    
    @width.setter
    def width(self, value):
        '''
        Method width for setting width
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Method height for retrieving width
        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''
        Method height for setting height
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def perimeter(self):
        '''
        static method for finding the perimeter of the rectangle
        '''
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def area(self):
        '''
        static method for finding the area of the rectangle
        '''
        return self.width * self.height

    def __del__(self):
        """
        Overwrites the inbuilt __del__ method
        """

        print("Bye rectangle...")
