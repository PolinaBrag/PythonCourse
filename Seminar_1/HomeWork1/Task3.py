from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
CHANCES = 10

secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, CHANCES + 1):
    print("Попытка номер ", i)
    num = int(input("Введите ваше число: "))
    if num > secret_num:
        print("Многовато")
    elif num == secret_num:
        print("Угадал, ты молодец!")
        break
    else:
        print("Маловато")



