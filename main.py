import random
import timeit

import pandas as pd
from find_algorithms import simple_search
from find_algorithms import binary_search
from find_algorithms import quick_sort

from Train import Train
from generation import generate

"""Размерность сгенерированных наборов данных"""
nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

"""Запись сгенерированных файлов в файл"""
# with pd.ExcelWriter("./trains.xlsx") as writer:
#     for i in nums:
#         pd.DataFrame(generate(i)).to_excel(writer, sheet_name=f"{i}", index=False)

"""Чтение из файла и запись в словарь, для дальнейшей сортировки"""
trains = {}
for i in nums:
    curr = pd.read_excel('./trains.xlsx', sheet_name=f'{i}').to_dict('records')
    curr_trains = []
    for train in curr:
        curr_trains.append(
            Train(train['Имя поезда'], train['Дата отправления'], train['Время отправления'], train['Время в пути'],
                  train['Номер поезда'],
                  train['Тип поезда'])
        )
    trains[i] = curr_trains

time_spent_simple = []
time_spent_binary_sort = []
time_spent_binary = []
time_spent_key = []

for j in nums:
    names = [k.train_name for k in trains[j]]
    key = Train(random.choice(names), "01/01/2000", "", "", "", "")

    """Поиск по ключу в массиве"""
    train_map = {}
    for train in trains[j]:
        train_map[train.train_name] = train
    starttime1 = timeit.default_timer()
    print(train_map[key.train_name].train_name)
    end1 = timeit.default_timer() - starttime1
    time_spent_key.append(end1)

    """Простой поиск"""
    starttime2 = timeit.default_timer()
    simple_search(trains[j], key)
    end2 = timeit.default_timer() - starttime2
    time_spent_simple.append(end2)

    """Бинарный поиск с сортировкой"""
    starttime3 = timeit.default_timer()
    quick_sort(trains[j], 0, len(trains[j]) - 1)
    binary_search(trains[j], 0, len(trains[j]), key)
    end3 = timeit.default_timer() - starttime3
    time_spent_binary_sort.append(end3)

    """Бинарный поиск"""
    starttime4 = timeit.default_timer()
    binary_search(trains[j], 0, len(trains[j]), key)
    end4 = timeit.default_timer() - starttime4
    time_spent_binary.append(end4)

print(f'time_spent_simple = {time_spent_simple}')
print(f'time_spent_binary_sort = {time_spent_binary_sort}')
print(f'time_spent_binary = {time_spent_binary}')
print(f'time_spent_key = {time_spent_key}')
