from datetime import datetime

"""Класс, описывающий объект поезда """
class Train:
    """Инициализирует объект, влючает :дату отправления, время отправления, время в пути, номер поезда, тип поезда"""
    def __init__(self, train_name, date, dep_time, trav_time, num, type):
        self.train_name = train_name
        self.date = datetime.strptime(date, '%m/%d/%Y')
        self.dep_time = dep_time
        self.trav_time = trav_time
        self.num = num
        self.type = type

    """Перегрузка оператора <"""
    def __lt__(self, other):
        return self.train_name < other.train_name

    """Перегрузка оператора <="""
    def __le__(self, other):
        return self.train_name <= other.train_name

    """Перегрузка оператора >"""
    def __gt__(self, other):
        return self.train_name > other.train_name

    """Перегрузка оператора >="""
    def __ge__(self, other):
        return self.train_name >= other.train_name

    """Перегрузка оператора =="""
    def __eq__(self, other):
        return self.train_name == other.train_name