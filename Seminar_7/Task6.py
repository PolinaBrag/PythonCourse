# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла. Переименование должно работать только для файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6
# из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов
# и расширение.
from pathlib import Path
import os.path


def rename_files(input_name: str, input_extension: str, diapason: list, output_name: str, count_nums: int,
                 output_extension: str):

    serial_num = '0' * count_nums
    # count_files = 0
    if os.path.exists(input_name + '.' + input_extension):
        # for i in range():
        Path(f'{input_name}.{input_extension}').rename(f'{input_name[(diapason[0]-1):diapason[1]]}'
                                                       f'{output_name}{serial_num}.{output_extension}')
    else:
        print("В директории нет файла с таким расширением")


if __name__ == '__main__':
    # with open('new_file.txt', 'a', encoding='utf-8') as f:
    #     f.write('Good bye')

    rename_files('new_file000', 'zip', [3, 6], 'new_file', 2, 'txt')

