#!/usr/bin/python3
"""
this is the module for this class for
the square class
"""


class Square():
    """
    this is the square class to calculte the perimetr area    
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ this is the initialisation function"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_mySquare(self):
        """ this is where the perimeter is calculated"""
        return (self.width + self.height) * 2

    def __str__(self):
        """ tis is what is returned when class called"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_mySquare())
