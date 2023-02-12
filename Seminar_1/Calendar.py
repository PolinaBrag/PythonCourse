SMALL_YEAR = 4
MIDDLE_YEAR = 100
BIG_YEAR = 400
REFORM = 1582

year = int(input("Введите год в формате 'уууу': "))

if year < REFORM:
    result = "Григорианский календарь еще не существует"
elif year % BIG_YEAR == 0:
    result = "Високосный"
elif year % SMALL_YEAR == 0:
    result = "Високосный"
elif year % MIDDLE_YEAR == 0:
    result = "Не високосный"
else:
    result = "Не високосный"
print(result)
