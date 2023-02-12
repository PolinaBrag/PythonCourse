# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def split_file_adress():
    path, type = input("Введите путь к файлу: ").split(".")
    name = path.split('\\')[-1]
    path = path.replace(name,'')
    return path, name, type


print(split_file_adress())
