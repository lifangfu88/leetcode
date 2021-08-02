"""
constructor, variable/function naming

"""


class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    _width = 0
    _height = 0

    def __init__(self, width, height):
        self._width = width
        self._height = height

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''

    def get_area(self):
        return self._width * self._height
