# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

list_keys = ["март", "апрель", "май"]
list_value = [3, 4, 5]


def create_dict(keys, values):
    new_dict = dict(zip(values, keys))
    return new_dict


res = create_dict(list_keys, list_value)
print(res)
