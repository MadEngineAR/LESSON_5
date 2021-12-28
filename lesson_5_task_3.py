"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности."""
from timeit import timeit
from collections import deque


# 1) Cравнение операций
# append, pop, extend списка и дека и сделать выводы что и где быстрее
# Данные операции быстрее у deque чем у обычных списков в два раза. Как и описано в документации.
def list_append(lst_sample):
    for i in range(n):
        lst_sample.append(i)
    return lst_sample


def deque_append(deq_sample):
    for i in range(n):
        deq_sample.append(i)
    return deq_sample


def list_extend(lst_sample):
    for i in range(n):
        lst_sample.extend([1, 2, 3])
    return lst_sample


def deque_extend(deq_sample):
    for i in range(n):
        deq_sample.extend([1, 2, 3])
    return deq_sample


def list_pop(lst_sample):
    for i in range(n):
        lst_sample.pop()
    return lst_sample


def deque_pop(deq_sample):
    for i in range(n):
        deq_sample.pop()
    return deq


# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее
# Данные операции быстрее у deque чем у обычных списков на несколько порядков!!!.
def list_append_left(lst_sample):
    for i in range(n):
        lst_sample.insert(i, 'new_el')
    return lst_sample


def deque_append_left(deq_sample):
    for i in range(n):
        deq_sample.appendleft('new_el')
    return deq_sample


def list_extend_left(lst_sample):
    for i in range(n):
        lst_sample.insert(i, [1, 2, 3])
    return lst_sample


def deque_extend_left(deq_sample):
    for i in range(n):
        deq_sample.extendleft([1, 2, 3])
    return deq_sample


def list_pop_left(lst_sample):
    for i in range(n):
        lst_sample.pop(i)
    return lst_sample


def deque_pop_left(deq_sample):
    for i in range(n):
        deq_sample.popleft()
    return deq


# 3) сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее
# Операции получения елементов быстрее у обычных списков. Как и описано в документации
def list_get_item(lst_sample):
    for i in range(10):
        el = lst_sample[i]
        return el


def deque_get_item(deq_sample):
    for i in range(10):
        el = deq_sample[i]
        return el


n = 100
lst = [i for i in range(1, 10)]
deq = deque(lst)
# 1)
print(f'Время выполнения list_append(lst) - {timeit("list_append(lst)", globals=globals(),number=1000)} ')
print(f'Время выполнения deque_append(deq) - {timeit("deque_append(deq)", globals=globals(),number=1000)}')
print(f'Время выполнения list_extend(lst) - {timeit("list_extend(lst)", globals=globals(),number=1000)}')
print(f'Время выполнения deque_extend(deq) - {timeit("deque_extend(deq)", globals=globals(),number=1000)}')
print(f'Время выполнения list_pop(lst) - {timeit("list_pop(lst)", globals=globals(),number=1000)}')
print(f'Время выполнения deque_pop(deq) - {timeit("deque_pop(deq)", globals=globals(),number=1000)}')
# 2)
print(f'Время выполнения list_append_left(lst) - {timeit("list_append_left(lst)", globals=globals(),number=100)} ')
print(f'Время выполнения deque_append_left(deq) - {timeit("deque_append_left(deq)", globals=globals(),number=100)}')
print(f'Время выполнения list_extend_left(lst) - {timeit("list_extend_left(lst)", globals=globals(),number=100)}')
print(f'Время выполнения deque_extend_left(deq) - {timeit("deque_extend_left(deq)", globals=globals(),number=100)}')
print(f'Время выполнения list_pop_left(lst) - {timeit("list_pop_left(lst)", globals=globals(),number=100)}')
print(f'Время выполнения deque_pop_left(deq) - {timeit("deque_pop_left(deq)", globals=globals(),number=100)}')
# 3)
print(f'Время выполнения list_get_item(lst) - {timeit("list_get_item(lst)", globals=globals(),number=100)} ')
print(f'Время выполнения deque_get_item(deq) - {timeit("deque_get_item(deq) ", globals=globals(),number=100)}')
