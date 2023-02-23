# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи

from Seminar_7.Task4 import make_files


def main_maker(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


if __name__ == '__main__':
    data = {
    'bin': 2,
    'zip': 3,
    }

    main_maker(data)