# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.

from time import time
print(f'Случайное число от 0 до 99 = {int(time() % 1 * 100)}')

# x(n + 1) = (a * x (n) + b) % m
m = 100
b = 3
a = 2
x = 1
c = 50

list = []

for i in range (c):
    x = (a * x + b) % m
    list.append(x)

print(list)