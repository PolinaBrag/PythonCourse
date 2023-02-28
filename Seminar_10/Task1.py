from math import pi


class Circumference:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    c1 = Circumference(10)
    print(c1.area())
    print(c1.perimeter())