"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
# Описал функции переноса ключа в конец словаря и удаления 1 го элемента. Перенос ключа быстрее с ordered_direct.
# Так не нужно удалять элемент и вставлять его снова. Операция удаления элемента быстрее с dict. В функциях удаления
# пришлось добавить update, т.к. при первом запуске пара удаляется, при последующих возникает ошибка.
# Честно говоря, мне пока не понятна необходимость сохранять порядок словаря. Но замеры показывают, что
# некоторые операции быстрее с ORDEREDDICT

from timeit import timeit
from collections import deque
from collections import OrderedDict


def dict_move_to_end(dct_sample):
    dct_sample.pop('x')
    dct_sample.update(x=1)
    return dct_sample


def ord_dict_move_to_end(dct_sample):
    dct_sample.move_to_end('x', last=True)
    return dct_sample


def dict_del_first_key(dct_sample):
    dct_sample.pop('y')
    dct_sample.update(y=10, last=False)
    return dct_sample


def ord_dict_del_first_key(dct_sample):
    dct_sample.popitem(last=False)
    dct_sample.update(y=10, last=False)
    return dct_sample


dict_1 = {'x': 1, 'y': 10, 'z': 100}
dict_2 = OrderedDict([('x', 1), ('y', 10), ('z', 100)])
print(f'Время dict_move_to_end - {timeit("dict_move_to_end(dict_1)", globals=globals(),number=1000)}')
print(f'Время ord_dict_move_to_end - {timeit("ord_dict_move_to_end(dict_2)", globals=globals(),number=1000)}')
print(f'Время dict_del_first_key - {timeit("dict_del_first_key(dict_1)", globals=globals(),number=1000)}')
print(f'Время ord_dict_del_first_key - {timeit("ord_dict_del_first_key(dict_2)", globals=globals(),number=1000)}')
