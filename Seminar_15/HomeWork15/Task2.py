import argparse
import logging

logging.basicConfig(level=logging.INFO, filename='TriangleCreate.log', encoding='utf-8')
logging.error('')
logger = logging.getLogger(__name__)


def check_triangle(a, b ,c):
    if (a+b) > c and (a+c) > b and (b+c) > a:
        if a == b == c:
            logger.info(f'Создан равносторонний треугольник со сторонами {a} , {b} и {c}')
            return "Треугольник равносторонний"
        elif a == b or a == c or b == c:
            logger.info(f'Создан равнобедренный треугольник со сторонами {a} , {b} и {c}')
            return "Треугольник равнобедренный"
        else:
            logger.info(f'Создан разносторонний треугольник со сторонами {a} , {b} и {c}')
            return "Треугольник разносторонний"
    else:
        logger.error(f'Треугольника со сторонами {a} , {b} и {c} не существует')
        return f'Треугольника со сторонами {a} , {b} и {c} не существует'


def parser_func():
    parser = argparse.ArgumentParser(description='Получаем стороны треугольника из строки')
    parser.add_argument('--sideA')
    parser.add_argument('--sideB')
    parser.add_argument('--sideC')
    args = parser.parse_args()

    a = int(args.sideA)
    b = int(args.sideB)
    c = int(args.sideC)
    return check_triangle(a, b, c)


if __name__ == '__main__':
    print(parser_func())