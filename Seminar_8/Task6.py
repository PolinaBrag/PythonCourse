# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import json
import os
from pathlib import Path
import pickle
import csv

def directory_info(directory: Path):
    dict_ = {}
    for dir_path, dir_name, file_name in os.walk(directory):
        dir_dict ={}
        print(f'\nРодительская директория: {dir_path}')
        for obj in Path(dir_path).iterdir():
            if obj.is_dir():
                print(f'{obj.name} директория', end='\n')
                dir_dict[obj.name] = 'директория'
                sum_size = 0
                for dir_path, dir_name, file_name in os.walk(obj):
                    if len(file_name) > 0:
                        for i in range(len(file_name) - 1):
                            sum_size += os.path.getsize(file_name[i])
                    if len(dir_name) > 0:
                        for i in range(len(dir_name) - 1):
                            sum_size += os.path.getsize(dir_name[i])
                print(f'Размер: {sum_size} байт')
                dir_dict[f'Размер {obj.name}'] = int(sum_size)
            elif obj.is_file():
                print(f'{obj.name} файл', end='\n')
                print(f'Размер: {os.path.getsize(obj)} байт')
                dir_dict[obj.name] = 'файл'
                dir_dict[f'Размер {obj.name}'] = int(os.path.getsize(obj))
            dict_.update({str(dir_path) : dir_dict})

    with open('json_file.json', 'w', encoding='utf-8') as f:
        json.dump(dict_, f,  ensure_ascii=False, indent=4)

    with open('pickle_file.pickle', 'wb') as f:
        pickle.dump(dict_, f)

    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=dict_,
                                   dialect='excel-tab',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerow(dict_)


directory_info(Path('../Seminar_1'))
