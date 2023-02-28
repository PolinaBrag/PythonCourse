class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width
        
    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.area())
    print(r1.perimeter())