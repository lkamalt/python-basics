# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

import numpy as np
from tools import get_number


def get_raised_to_power_op(val, power):
    """
    Возводит число val в степень power с использованием оператора возведения в степень **
    :param val: число, которое возводится в степень
    :type val: float
    :param power: показатель степени
    :type power: int
    :return: результат возведение числа val в степень power
    :type: float
    """
    return val ** power


def get_raised_to_power_loop(val, power):
    """
    Возводит число val в степень power с использованием цикла
    :param val: число, которое возводится в степень
    :type val: float
    :param power: показатель степени > 0
    :type power: int
    :return: результат возведение числа val в степень power
    :type: float
    """
    result = 2
    for p in range(2, power + 1):
        result *= val
    return result


def get_raised_to_power_cumprod(val, power):
    """
    Возводит число val в степень power с использованием функции кумулятивного умножения cumprod модуля numpy
    :param val: число, которое возводится в степень
    :type val: float
    :param power: показатель степени > 0
    :type power: int
    :return: результат возведения числа val в степень power
    :type: float
    """
    # Список из значений val, число повторений = power
    # Например, если val = 2, power = 3 -> val_list = [2, 2, 2]
    vals_list = [val] * power
    # Кумулятивное произведение элементов списка vals_list
    vals_list_cumprod = np.cumprod(vals_list)
    # Тогда последний элемент списка кумулятивного произведения будет нужным значением
    return vals_list_cumprod[-1]


def get_raised_to_neg_power(val, power):
    """
    Возводит число val в отрицательную степень power
    :param val: число, которое возводится в степень
    :type val: float
    :param power: показатель степени < 0
    :type power: int
    :return: результат возведения числа val в отрицательную степень power
    :type: float
    """
    # Вариант 1 - с использованием оператора возведения в степень **
    raised = get_raised_to_power_op(val, -power)

    # Вариант 2 - с использованием цикла
    # raised = get_raised_to_power_loop(val, -power)

    # Вариант 3 - с использованием функции кумулятивного умножения cumprod модуля numpy
    # raised = get_raised_to_power_cumprod(val, -power)

    # Возвращаем результат возведения в отрицительную степень и промежуточный результат - возведение
    # в такую же положительную степень (это только для вывода)
    return 1.0 / raised, raised


def main():
    """
    Основная функция
    Запрашивает у пользователя два значения: число, которое будет возведено в степень, само значение степени < 0
    Производит возведение числа в степень, выводит результут в консоль
    """
    # Запрашиваем у пользователя число, которое будет возводиться в степень
    val = get_number('1. Введите положительное число > 0 (для выхода нажмите q): ', float, lambda x: x > 0)

    # Если пользователь ввел q, то выходим
    if val is None:
        return

    # Запрашиваем у пользователя значение степени
    power = get_number('2. Введите целое отрицательное число (для выхода нажмите q): ', int, lambda x: x <= 0)

    # Если пользователь ввел q, то выходим
    if power is None:
        return

    # Возводит число в отрицательную степень
    result, mid_result = get_raised_to_neg_power(val, power)

    print(f'Результат: {val}^({power}) = 1.0 / {mid_result} = {result}')


# Вызов основной функции
main()
