# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import math

n1 = int(input('Введите числитель первой дроби: '))
d1 = int(input('Введите знаменатель первой дроби: '))
n2 = int(input('Введите числитель второй дроби: '))
d2 = int(input('Введите знаменатель второй дроби: '))

n_s = n1 * d2 + n2 * d1
d_s = d1 * d2

gcd_s = math.gcd(n_s, d_s)

n_s = n_s / gcd_s
d_s = d_s / gcd_s

print(f'сумма дробей: {int(n_s)}/{int(d_s)}')

n_m = n1 * n2
d_m = d1 * d2

gcd_m = math.gcd(n_m, d_m)

n_m = n_m / gcd_m
d_m = d_m / gcd_m

print(f'произведение дробей: {int(n_m)}/{int(d_m)}')

import fractions
f1 = fractions.Fraction(n1, d1)
f2 = fractions.Fraction(n2, d2)
print('сумма дробей с использованием fractions: ', f1 + f2)
print('произведение дробей с использованием fractions: ', f1 * f2)
