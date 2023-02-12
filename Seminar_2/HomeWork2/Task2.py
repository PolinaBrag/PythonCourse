from fractions import Fraction

first_fraction = input("Введите первую дробь в виде a/b: ")
second_fraction = input("Введите вторую дробь в виде a/b: ")

first_fraction = first_fraction.split("/")
second_fraction = second_fraction.split("/")

numerator_1 = int(first_fraction[0])
denominator_1 = int(first_fraction[1])
numerator_2 = int(second_fraction[0])
denominator_2 = int(second_fraction[1])

if denominator_1 != denominator_2:
    general_denominator = denominator_1 * denominator_2
    new_numerator_1 = denominator_2 * numerator_1
    new_numerator_2 = denominator_1 * numerator_2
    sum_of_fractions = str(new_numerator_1 + new_numerator_2) + '/' + str(general_denominator)
else:
    general_denominator = denominator_1
    sum_of_fractions = str(numerator_1 + numerator_2) + '/' + str(general_denominator)
print(f'{sum_of_fractions = }')

product_of_fractions = str(numerator_1 * numerator_2) + '/' + str(denominator_1 * denominator_2)
print(f'{product_of_fractions = }')

print("Проверка")
first_fraction = input("Введите первую дробь в виде a/b: ")
second_fraction = input("Введите вторую дробь в виде a/b: ")
a = Fraction(first_fraction)
b = Fraction(second_fraction)
sum_of_fractions = a + b
product_of_fractions = a * b
print(f'{sum_of_fractions = }')
print(f'{product_of_fractions = }')
