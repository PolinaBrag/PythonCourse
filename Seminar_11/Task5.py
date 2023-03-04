class Rectangle:
    """
    Создает прямоугольник и считает его периметр и площадь.
    """
    def __init__(self, length, width=None):
        """Инициализирует экземпляр класса Rectangle."""
        self.length = length
        self.width = length if width is None else width

    def area(self):
        """Возвращает площадь прямоугольника."""
        return self.width * self.length

    def perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.width + self.length)

    def __str__(self):
        """Возвращает строковое описание экземпляра класса Rectangle."""
        return f'Прямоугольник имеет периметр {self.perimeter()} и площадь {self.area()}'

    def __add__(self, other):
        """
        Возвращает новый экземпляр класса Rectangle,
        созданный из суммы периметров двух других экземпляров класса Rectangle.
        """
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        """
        Возвращает новый экземпляр класса Rectangle,
        созданный из разности периметров двух других экземпляров класса Rectangle.
        """
        new_perimeter = abs(self.perimeter() - other.perimeter)
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())
    print(r1)
    r2 = Rectangle(4, 5)
    print(r2.perimeter())
    print(r2)
    r3 = r2 - r1
    print(f' {r1 = }')
    print(f' {r3 = }')
    print(r3.perimeter())
    print(r3)