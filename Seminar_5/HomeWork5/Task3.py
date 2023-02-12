# Создайте функцию генератор чисел Фибоначчи

def fibonacci(num):
    first_num = 0
    second_num = 1
    print(first_num, second_num, sep='\n')
    for _ in range(num + 1):
        current_num = first_num + second_num
        first_num, second_num = second_num, current_num
        yield current_num


test_num = int(input("Введите какое количество чисел Фибоначчи неоюходимо вывести: "))
my_iter = iter(fibonacci(test_num))
for _ in range(test_num + 1):
    print(next(my_iter))
