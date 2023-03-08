# дескприптор

class TrueValue:
    def __init__(self, limit):
        self.limit = limit

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.is_true(value)
        setattr(instance, self.param_name, value)

    def is_true(self, value):
        if value <= self.limit:
            raise ValueError(f'Сторона должна быть > {self.limit}')


class Rectangle:
    length = TrueValue(10)
    width = TrueValue(10)

    def __init__(self, length, width=None):
        self._length = length
        self._width = length if width is None else width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

if __name__ == '__main__':
    r = Rectangle(2, 2)
    print(r.width, r.length)
    print(r.perimeter())
    r.length = 5
    r.width = 12
    print(r.width, r.length)
    print(r.perimeter())