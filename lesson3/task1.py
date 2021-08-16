# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

from tools import get_number


def get_division(num, denom):
    """
    Возвращает результат деления num на denom
    :param num: числитель
    :type num: float
    :param denom: знаменатель
    :type denom: float
    :return: результат деления
    :type: float
    """
    try:
        return num / denom
    except ZeroDivisionError as e:
        print('Деление на 0: ', e)


def main():
    """
    Основная функция
    Запрашивает у пользователя два числа - числитель и знаменатель
    Производит деление чисел, введенных пользователем, выводит результат
    :return:
    """
    num = get_number('1. Введите числитель (для выхода нажмите q): ', float, lambda x: True)
    if num is None:
        return

    # В функции запроса числа от пользователя можно запретить ввод нуля, тогда в данной конкретной задаче
    # обработка деления на 0 в функции get_division() можно опустить
    denom = get_number('2. Введите знаменатель (для выхода нажмите q): ', float, lambda x: True)
    if denom is None:
        return

    # Результат деления чисел, введенных пользователем
    result = get_division(num, denom)
    if result is not None:
        print(f'Результат деления: {num} / {denom} = {result}')


# Вызов основной функции
main()
