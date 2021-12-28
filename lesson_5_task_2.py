"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
from collections import defaultdict


# ВАРИАНТ 1 ООП
class Number16:
    def __init__(self, num_16):
        self.num_16 = num_16
        self.num_16_list = list(num_16)

    def __add__(self, other):
        # sum_hex = hex(int(self.num_16, 16) + int(other.num_16, 16)) - получется префикс. Решил через format.
        sum_16 = "{:x}".format(int(self.num_16, 16) + int(other.num_16, 16)).upper()
        return f'Cумма числа {self.num_16_list} и числа {other.num_16_list} равна {list(sum_16)}'

    def __mul__(self, other):
        mul_16 = "{:x}".format(int(self.num_16, 16) * int(other.num_16, 16)).upper()
        return f'Произведение числа {self.num_16_list} и числа {other.num_16_list} равна {list(mul_16)}'

    def __str__(self):
        return f''


print('Введите первое число_16 :')
num_1 = Number16(input())  # A2
print('Введите второе  число_16 :')
num_2 = Number16(input())  # C4F
print(num_1 + num_2)
print(num_1 * num_2)
