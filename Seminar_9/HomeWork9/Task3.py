# Декоратор, запускающий функцию нахождения корней с каждой тройкой чисел из csv файла

from typing import Callable
import csv
from random import randint


def create_csv(func: Callable):
    def wrapper(*args, **kwargs):
        # создаем новый csv файл, содержащий сгенерированные числа
        with open('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
            csv_write = csv.writer(f, dialect='excel-tab')
            for _ in range(100):
                nums = []
                for _ in range(3):
                    num = randint(1,1000)
                    nums.append(num)
                csv_write.writerow(nums)
        # считываем числа из csv файла, применяем к ним функцию и добавляем в список
        with open('csv_file.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
            res = []
            for row in reader:
                a = int(row[0])
                b = int(row[1])
                c = int(row[2])
                res.append(func(a, b, c))
        return res
    return wrapper()


@create_csv
def find_square_root(a: int, b: int, c: int):
    print(f'{a = }, {b = }, {c = }')
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Корней нет")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Корень один: {x = }")
    else:
        x = (-b + d ** 0.5) / 2 * a
        y = (-b - d ** 0.5) / 2 * a
        print(f"Корня два: {x = }, {y = }")

