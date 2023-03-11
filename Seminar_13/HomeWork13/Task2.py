class ProjectAnimalExceptions(Exception):
    pass


class AgeNegativeError(ProjectAnimalExceptions):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'AgeNegativeError: {self.message}'
        else:
            return f'Возраст не может быть отрицательным'

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        try:
            self.age = int(age)
            if self.age < 0:
                raise AgeNegativeError
        except ValueError as e:
            print('Возраст должен быть числом. Пусть возраст будет 1')
            self.age = 1


    def get_unique(self):
        pass


class Fish(Animal):
    def __init__(self, color, *args):
        self.color = color
        super().__init__(*args)

    def get_color(self):
        return f'Цвет рыбы {self.name} - {self.color}'


class Bird(Animal):
    def __init__(self, is_flies, name, age):
        self.is_flies = is_flies
        super().__init__(name, age)

    def can_flies(self):
        return f"The bird {self.name} flies? {self.is_flies}!"

    def __str__(self):
        spam = 'летает' if self.is_flies else 'ходит'
        return f'Перед нами птица по имени {self.name}. Ей {self.age} лет. Эта птица {spam}'


class Dog(Animal):
    def __init__(self, height, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):
        if self.height < 0.5:
            return f'{self.name} маленький собачонок'
        elif 0.5 < self.height < 1:
            return f'{self.name} огромный пес'

class AnimalCreator:

    def create_animal(self, animal_type, *args):
        if animal_type == "Dog":
            return Dog(*args)
        elif animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Fish":
            return Fish(*args)


if __name__ == '__main__':
    b = Bird(True, 'Птенец', 5)
    print(b)

