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

     def update(self, *args, **kwargs):
        """
        Update the Square.
        Args:
            *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
