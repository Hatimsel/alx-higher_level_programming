#!/usr/bin/python3
"""First Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation the class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        """width getter"""
        return self.__width

    # @width.setter
    def set_width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def get_height(self):
        """height getter"""
        return self.__height

    # @height.setter
    def set_height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def get_x(self):
        """x getter"""
        return self.__x

    # @x.setter
    def set_x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def get_y(self):
        """y getter"""
        return self.__y

    # @y.setter
    def set_y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """return the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays in stdout the rectangle with characters #"""
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range (self.__x):
                    print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """updating __str__ special method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """updatig the class Rectangle"""
        attr_list = ["id", "width", "height", "x", "y"]
        i = 0
        if args:
            for arg in args:
                if i >= len(attr_list):
                    return

                setattr(self, attr_list[i], arg)
                # self.__setattr__(attr_list[i], arg)
                i += 1
        for key, value in kwargs.items():
            # self.__setattr__(key, value)
            setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict represantation of Rectangle class"""
        dict = {"id": self.id, "width": self.width, "height": self.height\
                , "x": self.x, "y": self.y}
        return dict
