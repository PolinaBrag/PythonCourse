# Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики
import Task5


class AnimalCreator:

    def create_animal(self, animal_type, *args):
        if animal_type == "Dog":
            return Task5.Dog(*args)
        elif animal_type == "Bird":
            return Task5.Bird(*args)
        elif animal_type == "Fish":
            return Task5.Fish(*args)


if __name__ == '__main__':
    ac = AnimalCreator()
    dog = ac.create_animal("Dog", 0.3, 'Макс', 5)
    print(dog.get_height())
    fish = ac.create_animal("Fish", 'золотой', 'Долли', 1)
    print(fish.get_color())
    bird = ac.create_animal("Bird", True, 'Птенец', 2)
    print(bird)
