# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года — 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['existence_check_date', 'leap_year_check']

SMALL_YEAR = 4
MIDDLE_YEAR = 100
BIG_YEAR = 400
REFORM = 1582
MONTHS = 12
ZERO = 0
MAX_DAYS = 31
MAX_YEAR = 9999


def existence_check_date(date):
    return ZERO < int(date.split(".")[2]) <= MAX_YEAR and ZERO < int(date.split(".")[1]) <= MONTHS \
        and ZERO < int(date.split(".")[0]) <= MAX_DAYS


def leap_year_check(date):
    year = int(date.split(".")[2])
    if year < REFORM:
        result = "Григорианский календарь еще не существует"
    elif year % BIG_YEAR == ZERO:
        result = "Високосный"
    elif year % SMALL_YEAR == ZERO:
        result = "Високосный"
    elif year % MIDDLE_YEAR == ZERO:
        result = "Не високосный"
    else:
        result = "Не високосный"
    return result


if __name__ == '__main__':
    date_ = input("Введите дату в формате DD.MM.YYYY: ")
    print(existence_check_date(date_))
    print(leap_year_check(date_))