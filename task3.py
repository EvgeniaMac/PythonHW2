# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.


import math

n = int(input('Введите число: '))
a = []
sum = 0
for i in range(n):
    a.append(round(math.pow((1+1/n), n), 2))
    sum = round(sum + a[i], 2)
print(a, sep=',')
print(sum)
