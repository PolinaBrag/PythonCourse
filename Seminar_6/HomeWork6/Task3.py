# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они
# не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход
# восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если
# ферзи не бьют друг друга верните истину, а если бьют — ложь
from random import randint

COUNT = 8


def check_queens(list_num):
    x = [list_num[i] for i in range(0, len(list_num), 2)]
    y = [list_num[i] for i in range(1, len(list_num) + 1, 2)]

    fight = False
    for i in range(COUNT):
        for j in range(i + 1, COUNT):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                fight = True

    return not fight


def random_coordinates():
    list_num = []
    for i in range(COUNT*2):
        list_num.append(randint(1, 8))
    return list(list_num)


if __name__ == '__main__':
    # user_nums = [int(i) for i in input("Введите 8 пар чисел с координатами через пробел: ").split()]
    # print(check_queens(user_nums))

    count_successful_placement = 0

    while count_successful_placement < 5:
        coord = random_coordinates()
        res = check_queens(coord)
        if res:
            count_successful_placement += 1
            print(*coord)

