# Задача №8: Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
x, y = int(input("Введите координату x: ")), int(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка в 1-ой четверти координатной плоскости")
elif x < 0 and y > 0:
    print("Точка во 2-ой четверти координатной плоскости")
elif x < 0 and y < 0:
    print("Точка в 3-ей четверти координатной плоскости")
elif x > 0 and y < 0:
    print("Точка в 4-ой четверти координатной плоскости")
elif x == 0:
    print("Точка на оси Y")
else:
    print("Точка на оси X")