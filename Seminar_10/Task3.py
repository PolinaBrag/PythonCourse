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


if __name__ == '__main__':
    p1 = Person('Иван', 'Иванов', 23)
    print(p1.get_age())
    p1.birthday()
    print(p1.get_age())
    print(p1.get_full_name())
    print(p1.name)
