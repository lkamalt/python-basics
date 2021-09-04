import numpy as np
from tools import get_number, quit_symbol


class CustomZeroDivisionError(Exception):
    """ Класс исключений, обрабатывающий ситуацию деления на 0 """
    pass


def get_division(num, denom):
    """
    Возвращает результат деления num на denom
    Если знаменатель равен 0, то генерируется исключение CustomZeroDivisionError
    :param num: числитель
    :type num: float
    :param denom: знаменатель
    :type denom: float
    :return: результат деления
    :type: float
    """
    if np.isclose(denom, 0):
        raise CustomZeroDivisionError('Деление на 0!')
    return num / denom


def main():
    """
    Основная функция
    Запрашивает у пользователя два числа - числитель и знаменатель
    Производит деление чисел, введенных пользователем, выводит результат
    """
    quit_symbol_upper = quit_symbol.upper()

    num = get_number(f'1. Введите числитель (для выхода введите {quit_symbol_upper}): ', float)
    if num is None:
        return

    denom = get_number(f'2. Введите знаменатель (для выхода введите {quit_symbol_upper}): ', float)
    if denom is None:
        return

    # Результат деления чисел, введенных пользователем
    try:
        print(f'Результат деления: {num} / {denom} = {get_division(num, denom)}')
    except CustomZeroDivisionError as e:
        print(e)


main()
