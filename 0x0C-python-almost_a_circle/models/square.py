#!/usr/bin/python3
"""The square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiating the class"""
        super().__init__(x, y, id, size, size)

    def __str__(self):
        """Adjusting str special method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def get_size(self):
        """size getter"""
        return self.width
    
    def set_size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updating the square class"""
        attr_list = ["id", "size", "x", "y"]
        if args:
            i = 0
            for arg in args:
                if i >= len(args):
                    return
                self.__setattr__(attr_list[i], arg)
                i += 1
        for key, value in kwargs.items:
            self.__setattr__(key, value)

    def to_dictionary(self):
        """returns the dict representation of a square"""
        dict = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return dict
