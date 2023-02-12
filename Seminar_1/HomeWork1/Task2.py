ZERO = 0
ONE_HUNDRED_THOUSANDS = 100_000
ONE = 1

delimeters = 0

while True:
    numb = int(input('Введите ваше число от 0 до 100 000: '))
    if ZERO <= numb < ONE_HUNDRED_THOUSANDS:
        break
for i in range(ONE, numb + ONE):
    if i > ONE and numb % i == ZERO:
        delimeters += 1
if delimeters == ONE:
    res = 'Число простое'
else:
    res = 'Число составное'
print(res)
