# логирование деления на 0

import logging


logging.basicConfig(level=logging.ERROR, filename='ZeroDivisionError.log', encoding='utf-8')
logger = logging.getLogger(__name__)


def func_div_two(a, b) -> float:
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(f'Ошибка деления числа {a} на число {b}')
        return float('inf')
    return res


if __name__ == '__main__':
    print(func_div_two(8, 0))