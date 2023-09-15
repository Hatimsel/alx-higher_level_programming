#!/usr/bin/python3
"""
Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square instantiation
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns a formatted representation of the Square class
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        super(Square, Square).width.fset(self, size)
        super(Square, Square).height.fset(self, size)

    def update(self, *args, **kwargs):
        """
        Updates the class Square
        """
        if len(args) > 0:
            attr_tpl = ('id', 'size', 'x', 'y')

            for i, arg in enumerate(args):
                if i >= len(attr_tpl):
                    break
                setattr(self, attr_tpl[i], arg)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """
        Square instance to dictionary representation
        """
        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic
