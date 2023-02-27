# Генерация csv файла с тремя случайными числами в каждой строке (100 - 1000 строк)
import csv
from random import randint


def create_csv():
    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel-tab')

        for _ in range(100):
            nums = []
            for _ in range(3):
                num = randint(1,1000)
                nums.append(num)
            csv_write.writerow(nums)


create_csv()

