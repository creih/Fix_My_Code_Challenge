#!/usr/bin/python3
"""
this is the square class module
"""

class square():
    """this is the class in question"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ this is the initialisation of class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return self.height + self.width + self.height + self.width

    def __str__(self):
        """ this is the returned string for class """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
