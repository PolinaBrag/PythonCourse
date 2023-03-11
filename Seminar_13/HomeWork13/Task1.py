# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from math import pi

ZERO = 0


class ProjectCircumferenceExceptions(Exception):
    pass


class RadiusZeroError(ProjectCircumferenceExceptions):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'RadiusError: {self.message}'
        else:
            return f'Радуис не может быть равен 0, это точка, а не круг'


class RadiusNegativeError(ProjectCircumferenceExceptions):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'RadiusError: {self.message}'
        else:
            return f'Радуис не может быть меньше 0, круг не существует.'


class Circumference:

    def __init__(self, radius):
        if radius == ZERO:
            raise RadiusZeroError
        elif radius < 0:
            raise RadiusNegativeError
        else:
            self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    c1 = Circumference(0)
    print(c1.area())
    print(c1.perimeter())