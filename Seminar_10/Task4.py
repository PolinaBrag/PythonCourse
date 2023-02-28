from random import randint

class Person:

    def __init__(self, name, surname, age, hobby=None):
        self.name = name
        self.surname = surname
        self.__age = age
        self.hobby = hobby

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return self.__age


class Employee(Person):
    _DIV = 7
    COUNT_NUM = 6

    def __init__(self, idx, *args):
        min_num = 10 ** (self.COUNT_NUM - 1)
        max_num = 10 ** self.COUNT_NUM - 1
        if idx < min_num or idx > max_num:
            self.idx = randint(min_num, max_num)
        else:
            self.idx = idx
        # self.lvl = self.idx % self._DIV
        # self.access_lvl = sum(int(i) for i in str(self.id_num)) % 7
            self.lvl = sum(int(i) for i in str(self.idx)) % self._DIV
            super().__init__(*args)


if __name__ == '__main__':
    emp = Employee(123457, 'Иван', 'Иванов', 23)
    print(emp.name)