# В модуль с проверкой даты добавьте возможность запуска
# в терминале с передачей даты на проверку.

from sys import argv

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
    print(existence_check_date(argv[1]))
    print(leap_year_check(argv[1]))