# Создайте класс Матрица. Добавьте методы для вывода на печать, сравнения, сложения и умножения матриц.
from random import randint


class Matrix:
    def __init__(self, row_count, column_count):
        self.row_count = int(row_count)
        self.column_count = int(column_count)
        self.matrix = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def random_fill_matrix(self):
        for row in range(self.row_count):
            chank = []
            for col in range(self.column_count):
                chank.append(randint(1, 9))
            self.matrix.append(chank)

    def __str__(self):
        return '\n'.join('  '.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        if self.row_count != other.row_count or self.column_count != other.column_count:
            return 'Нельзя сложить матрицы разного размера'
        else:
            new_matrix = Matrix(self.row_count, self.column_count)
            for row in range(self.row_count):
                chank = []
                for col in range(self.column_count):
                    chank.append(self.matrix[row][col] + other.matrix[row][col])
                new_matrix.matrix.append(chank)
        return new_matrix

    def __eq__(self, other):
        if self.row_count != other.row_count or self.column_count != other.column_count:
            return False
        else:
            for row in range(self.row_count):
                for col in range(self.column_count):
                    if self.matrix[row][col] != other.matrix[row][col]:
                        return False
            return True


if __name__ == '__main__':
    m1 = Matrix(3, 3)
    m1.random_fill_matrix()
    print(m1)
    print()
    m2 = Matrix(3, 3)
    m2.random_fill_matrix()
    print(m2)
    print()
    m3 = m1 + m2
    print(m3)
    print()
    print(m1 == m2)

