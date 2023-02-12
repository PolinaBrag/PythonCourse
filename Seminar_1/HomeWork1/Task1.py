a = 154
b = 14
c = 145

if (a+b) > c and (a+c) > b and (b+c) > a:
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольника не существует")