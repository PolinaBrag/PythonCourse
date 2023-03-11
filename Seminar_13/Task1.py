def get_num() -> float | int:
    while True:
        value = input('Введите число: ')

        try:
            num = int(value) if '.' not in value else float(value)
            return num
        except ValueError:
            print('Неверные данные')


if __name__ == '__main__':
    print(get_num())