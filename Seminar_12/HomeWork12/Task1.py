# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
from pathlib import Path
import csv

class TrueValue:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.is_true(value)
        setattr(instance, self.param_name, value)

    def is_true(self, value):
        if not value.isalpha():
            raise ValueError(f'Значение {value} должно состоять только из букв!')
        if not value.istitle():
            raise ValueError(f'Значение {value} должно начинаться с заглавной буквы!')


class Student:
    first_name = TrueValue()
    last_name = TrueValue()
    surname = TrueValue()

    def __init__(self, first_name: str, last_name: str, surname: str):
        self._first_name = first_name
        self._last_name = last_name
        self._surname = surname
        self.objects = []

    def __enter__(self):
        csv_file = Path('csv_file.csv').open('r', encoding='utf-8')
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            dict_ = {}
            subject, grade, *test_res = row
            dict_['Предмет'] = subject
            dict_['Оценка'] = int(grade)
            dict_['Тест'] = test_res
            self.objects.append(dict_)
        return self.objects

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.csv_file.close()
        pass

    def __str__(self):
        return f'Ученика зовут {self._last_name} {self._first_name} {self._surname}'

    def average_tests(self):
        for i in self.objects:
            for j in range(len(i['Тест'])):
                i['Тест'][j] = int((i['Тест'][j]))
            av_grade = sum(i['Тест']) / len(i['Тест'])
            sub = i['Предмет']
            print(f'Средняя оценка по тестам по предмету {sub} равна {av_grade}')

    def average_grades(self):
        sum_ = 0
        count = 0
        for i in self.objects:
            sum_ += i['Оценка']
            count += 1
        average_grade = sum_ / count
        print(f'Средняя оценка по всем предметам равна {average_grade}')


if __name__ == '__main__':
    s = Student('Иван', 'Иванов', 'Иванович')
    print(s)
    s.first_name = 'Костя'
    print(s)
    with s as f:
        print(f)
    s.average_tests()
    s.average_grades()