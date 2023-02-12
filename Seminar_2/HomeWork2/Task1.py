ZERO = 0
HEX = 16

n = int(input("Введите ваше число: "))
work_num = n
b = ""

while work_num > 0:
    remainder = work_num % HEX
    if 16 >= remainder >= 10:
        match remainder:
            case 16:
                b = "10" + b
            case 15:
                b = "F" + b
            case 14:
                b = "E" + b
            case 13:
                b = "D" + b
            case 12:
                b = "C" + b
            case 11:
                b = "B" + b
            case 10:
                b = "A" + b
    else:
            b = str(remainder) + b
    work_num = int(work_num / HEX)
print(b)

print(hex(n))