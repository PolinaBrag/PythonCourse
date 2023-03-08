# геттер и сеттер + экономия памяти через слоты

class Rectangle:

    __slots__ = ('_length', '_width') # замена словаря на слот -> экономия памяти

    def __init__(self, length, width=None):
        self._length = length
        self._width = length if width is None else width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length_value):
        if length_value > 0:
            self._length = length_value
        else:
            raise ValueError(f'Длина должна быть больше нуля. Передано {length_value}')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value):
        if width_value > 0:
            self._width = width_value
        else:
            raise ValueError(f"Value cannot be below zero. Provided value: {width_value}")


if __name__ == '__main__':
    r = Rectangle(2, 2)
    print(r.width, r.length)
    print(r.perimeter())
    r.length = 5
    r.width = 12
    print(r.width, r.length)
    print(r.perimeter())