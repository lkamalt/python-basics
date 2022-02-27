# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import numpy as np
from tools import convert_to_number, get_data_from_file


def get_employees_info(data):
    """
    Возвращает словарь, составленный из данных файла
    Словарь вида: имя сотрудника - оклад сотрудника
    :param data: список строк из файла
    :type data: List[str]
    :return: словарь с информацией о каждом сотруднике
    :type: dict{str: float}
    """
    employees_info = {}
    if data is None:
        return employees_info

    for d_str in data:
        # Считаем, что в файле записаны только фамилия и оклад, причем эти значения разделены пробелом
        d_list = d_str.split()
        if len(d_list) < 2:
            continue

        # Имя сотрудника и его зарплата
        name, salary = d_list[0], convert_to_number(d_list[1], float, np.nan)
        # Записываем в словарь сотрудника и его зарплату
        employees_info[name] = salary

    return employees_info


def get_employees_with_min_salary(employees_info, min_salary):
    """
    Возвращает список фамилий сотрудников, оклад которых меньше минимального
    :param employees_info: словарь с ифнормацией о сотрудниках: имя сотрудника - оклад сотрудника
    :type employees_info: dict{str, float}
    :param min_salary: величина минимального оклада
    :type min_salary: float
    :return: список сотрудников с окладом < минимального
    :type: List[str]
    """
    return [name for name in employees_info.keys() if employees_info[name] < min_salary]


def get_employees_avg_salary(employees_info):
    """
    Возвращает величину среднего оклада по всем сотрудникам
    :param employees_info: словарь с ифнормацией о сотрудниках и их окладах вида: имя сотрудника - оклад сотрудника
    :type employees_info: dict{str, float}
    :return: средний оклад по всем сотрудников
    :type: float
    """
    return np.nanmean(list(employees_info.values()))


def main():
    """
    Основная функция
    Выводит средний оклад по всем сотрудниками и список фамилий сотрудников с окладом < минимального оклада
    Минимальный оклад задается, данные по сотрудникам и их окладам считываются их файла
    """
    # Минимальный оклад
    min_salary = 20000.0

    # Данные по сотрудникам из файла
    data = get_data_from_file('task3.txt')
    # Словарь с данными из файла: имя сотрудника - оклад сотрудника
    employees_info = get_employees_info(data)

    # Средний оклад по всем сотрудникам
    avg_salary = get_employees_avg_salary(employees_info)
    # Фамилии сотрудников с окладом < минимального
    min_salary_names = get_employees_with_min_salary(employees_info, min_salary)

    print('Средняя зарплата сотрудников: ', avg_salary)
    print(f'Сотрудники с величиной оклада < {min_salary}: {", ".join(min_salary_names)}')


main()
