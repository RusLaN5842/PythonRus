#Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

x, y = 4, 6
if x > y: big_num = x
else: big_num = y
while(True):
    if (big_num % x == 0) and (big_num % y == 0):
        result = big_num
        break
    big_num += 1
    print(result)