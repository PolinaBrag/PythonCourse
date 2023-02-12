ZERO = 0
TEN = 10
HUNDRED = 100
THOUSAND = 1000
POW = 2

while True:
    numb = int(input('Введите ваше число от 1 до 999: '))
    if ZERO < numb < THOUSAND:
        break
if numb < TEN:
    res = numb ** POW
elif TEN <= numb < HUNDRED:
    res = (numb % TEN) * (numb // TEN)
else:
    res = numb % TEN * 100 + numb // TEN % TEN * 10 + (numb - (numb % HUNDRED)) // HUNDRED
print(res)