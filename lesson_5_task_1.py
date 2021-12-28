from collections import namedtuple

"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

"""Класс collections.namedtuple()"""
Company = namedtuple('Company', 'name profit')
companies = []
avg_all_companies = 0
print(f'Введите количество предприятий для расчета прибыли ')
n = int(input())
for i in range(n):
    i += 1
    print(f'Введите название преприятия ')
    name_comp = input()

    try:
        input_list = input("Через пробел введите прибыль предприятия за каждый квартал(Всего 4 квартала) ").split()
        num_list = list(map(int, input_list))
        if len(num_list) <= 4:
            profit: int = sum(num_list)
            companies.append(Company(name_comp, profit))
            avg_all_companies = (avg_all_companies + profit) / len(companies)  
        else:
            raise ValueError
    except ValueError:
        print('Ошибка ввода.В году 4 квартала')
        exit(1)
print(f'Средняя годовая прибыль всех предприятий {avg_all_companies}')
lower_profit = [company.name for company in companies if company.profit < avg_all_companies]
higher_profit = [company.name for company in companies if company.profit > avg_all_companies]
print('Предприятия, с прибылью выше среднего значения:')
print(*higher_profit, sep='\n')
print('Предприятия, с прибылью ниже среднего значения:')
print(*lower_profit, sep='\n')
