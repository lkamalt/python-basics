# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков). Итоговый список сохранить в виде
# json-объекта в соответствующий файл.

import numpy as np
import re

from tools import convert_to_number, get_data_from_file, serialize_data_json, deserialize_data_json

# Формы собственности
ownerships = ['ООО', 'ЗАО', 'ИП', 'ПАО', 'ОАО']


def get_firms_info(data):
    """
    Возвращает словарь, составленный из данных файла
    Словарь вида: название фирмы - прибыль (убыток)
    :param data: список строк из файла
    :type data: List[str]
    :return: словарь с информацией о каждой фирме
    :type: dict{str, float}
    """
    firms_info = {}
    if data is None:
        return firms_info

    for d_str in data:
        # Список из имени и строки с прибылью
        name_and_info = get_splitted_by_ownership(d_str)
        if len(name_and_info) < 2:
            continue

        # Выручка и издержки компании в виде одного списка
        info = [convert_to_number(v, float) for v in name_and_info[1].split()]
        if None in info:
            continue

        # Расшепляем массив на отдельные переменные
        proceeds, costs = info
        # Записываем в словарь название фирмы и её прибыль (убыток)
        firms_info[name_and_info[0]] = proceeds - costs

    return firms_info


def get_splitted_by_ownership(s):
    """
    Разбивает входную строку по форме собственности из списка ownerships
    :param s: входная строка, которая содержит название, форму собственности, выручку и издержки
    :type s: str
    :return: список подстрок, разделенные словом из ownerships
    :type: List[str]
    """
    # Разбирваем строку по форме собственности
    s_splitted = re.split(r'|'.join(ownerships), s, re.IGNORECASE)
    # Удаляем лишние пробелы и контрольные символы по краям каждого слова
    return [s.strip() for s in s_splitted]


def get_firms_avg_profit(firms_info):
    """
    Возвращает значение средней прибыли по всем компаниям
    :param firms_info: словарь с информацией о каждой фирме: название фирмы - прибыль (убыток)
    :type firms_info: dict{str: float}
    :return: средняя прибыль по всем фирмам
    :type: float
    """
    # Список значений прибыли каждой компании
    profits = [p for p in firms_info.values() if p > 0]
    return np.mean(profits)


def main():
    """
    Основная функция
    Производится считывание данных по фирмам из файла, каждая строка файла содержит информацию об одной фирме
    Составляется словарь, каждый элемент которого содержит название и прибыль (убыток) фирмы
    Вычисляется средняя прибыль по компаниям
    Полученная информация записывается в json
    """
    # Данные по компаниям из файла (список строк)
    data = get_data_from_file('task7.txt')

    # Словарь: название фирмы - прибыль (убыток)
    firms_info = get_firms_info(data)
    # Средняя прибыль по всем фирмам
    avg_profit = get_firms_avg_profit(firms_info)

    # Словарь с информацией о компаниях и средней прибыли
    profit_data = [firms_info, {'average_profit': avg_profit}]
    # Сохраняем в json
    serialize_data_json('task7.json', profit_data)

    # Извлекаем данные из json
    profit_data = deserialize_data_json('task7.json')
    print('Данные о компаниях и средней прибыли после десериализации: ', profit_data)


main()
