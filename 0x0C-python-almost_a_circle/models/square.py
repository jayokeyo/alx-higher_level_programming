#!/usr/bin/python3
'''
Defines class Square
'''
class Square(Rectangle):
    '''
    class Square with Class constructor: def __init__(self, size, x=0, y=0, id=None):
    and __str__ method should return [Square] (<id>) <x>/<y> - <size>
    '''
    def __init__(self, size, x = 0, y = 0, id = None):
        '''
        class constructor of class Square
        Args:
            size - side of square
            x - displacement of square along x axis
            y - displacement of square along y axis
            id - id of object
        '''
        super.__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Overides inbuilt method __str__
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        Getter
        """
        return self.width

    @size.setter
    def size(self, value):
        '''
        Setter
        '''
        self.width = value
        self.height = value
