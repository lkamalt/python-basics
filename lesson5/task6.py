# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

import re
from tools import convert_to_number, get_data_from_file


def get_subj_info(data):
    """
    Возвращает словарь, составленный из данных файла
    Словарь вида: название предмета - количество занятий
    :param data: список строк из файла
    :type data: List[str]
    :return: словарь с информацией о каждом предмете
    :type: dict{str, int}
    """
    subj_info = {}
    if data is None:
        return subj_info

    for d_str in data:
        # Считаем, что название предмета отделено от строки с количеством занятий двоеточием
        d_list = d_str.split(':')
        if len(d_list) < 2:
            continue

        # Название и строка с количеством занятий предмета
        name, counts_str = d_list
        # Список количества часов предмета
        counts = [convert_to_number(c, undef_value=0) for c in get_subj_count_replace(counts_str)]
        # Записываем в словарь название предмета и его количество занятий (количество извлекаем из строки counts_str)
        subj_info[name] = sum(counts)

    return subj_info


def get_subj_count_find(counts_str):
    """
    Возвращается список из чисел, извлеченных из строки counts_str
    :param counts_str: строка с числами
    :type counts_str: str
    :return: список чисел
    :type: List[int]
    """
    counts = []
    # Предполагается, что количество занятий с пояснениеями разделеы между собой пробелом
    for c in counts_str.split():
        # Работает только если после каждого количества сразу идет скобка с пояснением
        idx = c.find('(')
        if idx > 0:
            counts.append(c[:idx])
    return counts


def get_subj_count_re(s):
    """
    Возвращается список из чисел, извлеченных из строки s с помощью регулярки
    :param s: строка с числами
    :type s: str
    :return: список чисел
    :type: List[int]
    """
    # Список всех чисел (тип str), найденных в строке counts_str
    return re.findall(r'\d+', s)


def get_subj_count_replace(s):
    """
    Возвращается список из чисел, извлеченных из строки s с помощью замены подстрок
    :param s: строка с числами
    :type s: str
    :return: список чисел
    :type: List[int]
    """
    counts_str_clear = s.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
    return counts_str_clear.split()


def print_subj_info(subj_info):
    """
    Выводит в консоль название каждого предмета и количество занятий по нему
    :param subj_info: словарь с информацией о каждом предмете: название предмета - количество занятий
    :type subj_info: dict{str, int}
    """
    for name, count in subj_info.items():
        print(f'{name:>15}: {count}')


def main():
    """
    Основная функция
    Производится считывание данных по учебным предметам из файла
    Каждая строка файла содержит информацию (количество занятий) об одном предмете
    Составляется словарь, каждый элемент которого содержит название и количество занятий предмета
    Полученный словарь с информацией о предметах выводится в консоль
    """
    # Данные по предметам из файла (список строк)
    data = get_data_from_file('task6.txt')
    # Словарь: название предмета - количество занятий
    subj_info = get_subj_info(data)
    # Выводим количество занятий по всем предметам
    print_subj_info(subj_info)


main()
