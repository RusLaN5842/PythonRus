#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
#на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
#positions = [1, 3, 6]).
import random
def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs

# улучшение 

#lst_number = [i for i in range(-n, n+1)]
#write_file(n)
#lst_index = read_file()
#prod = 1
#for i in range(len(lst_index)):
#    prod *= lst_number[lst_index[i]]
#print(f"Результат равен = {prod}")