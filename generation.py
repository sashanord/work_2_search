"""Модуль для генерации объектов типа Train"""
import datetime
import random
import string

"""Список возможных типов поезда"""
types = ['скорый', 'пассажирский', 'товарный']

"""Вспомогательная функция, возвращает сгенерированную дату"""
def generate_date():
    d = datetime.date(random.randrange(2000, 2023), random.randrange(1, 13), random.randrange(1, 28))
    return d.strftime("%m/%d/%Y")

"""Вспомогательная функция, возвращает сгенерированное время"""
def generate_time():
    h = random.randrange(0, 24)
    h = f'0{h}' if h < 10 else str(h)

    m = random.randrange(0, 60)
    m = f'0{m}' if m < 10 else str(m)

    return f'{h}:{m}'

"""Возвращает сгенерированное имя поезда"""
def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

"""Возвращает сгенерированнуый словарь для записи в DataFrame, каждое значение-список длины n"""
def generate(n):
    final_dict = {}
    names = []
    dates = []
    dep_time = []
    trav_time = []
    num = []
    type_ = []
    for i in range(n):
        names.append(generate_name())
        dates.append(generate_date())
        dep_time.append(generate_time())
        trav_time.append(round(random.uniform(1, 48), 2))
        num.append(random.randrange(1, 1000))
        type_.append(types[random.randrange(0, 3)])
    final_dict['Имя поезда'] = names
    final_dict['Дата отправления'] = dates
    final_dict['Время отправления'] = dep_time
    final_dict['Время в пути'] = trav_time
    final_dict['Номер поезда'] = num
    final_dict['Тип поезда'] = type_
    return final_dict
