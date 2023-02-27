# Поиск корней квадратного уравнения

def find_square_root(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Корней нет")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Корень один: {x = }")
    else:
        x = (-b + d ** 0.5) / 2 * a
        y = (-b - d ** 0.5) / 2 * a
        print(f"Корня два: {x = }, {y = }")

find_square_root(3, -4, 94)