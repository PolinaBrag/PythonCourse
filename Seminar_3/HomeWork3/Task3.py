from operator import itemgetter

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

baggage = {'аптечка': 1, 'одежда': 3, 'посуда': 2, 'продукты': 4, 'палатка': 7}

load_capacity = int(input("Введите грузоподъемность рюкзака в кг: "))

sorted_baggage = dict(sorted(baggage.items(), key=itemgetter(1), reverse=True))


def check_weight(new_dict):
    weight = 0
    for key, value in new_dict.items():
        weight += new_dict.get(key)
    return weight


check_weight(sorted_baggage)

if load_capacity >= check_weight(sorted_baggage):
    print('В рюкзак все влезет')
else:
    while check_weight(sorted_baggage) > load_capacity:
        sorted_baggage.popitem()
        check_weight(sorted_baggage)
    print("Берем с собой только: ")
    for key, value in sorted_baggage.items():
        print(key)
