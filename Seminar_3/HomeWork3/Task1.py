# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
REPEAT = 2
new_list = []
for el in list_num:
    if list_num.count(el) >= REPEAT:
        if el not in new_list:
            new_list.append(el)
print(new_list)