# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369

import sys
from tools import convert_to_number, is_correct


def get_n_sum(n_str):
    """
    Возвращает сумму чисел вида: n + nn + nnn
    n_str - число n в виде строки
    """
    sum_n = 0
    for i in range(1, 4):
        n = int(n_str * i)
        print(f'{"n" * i} = {n}')
        sum_n += n

    return sum_n


# Введенное число в виде строки
n_str = input('Введите целое число > 0: ')

# Пробуем сконвертировать
n_int = convert_to_number(n_str)
# Проверяем, что не None и > 0, иначе заврешаем программу
if not is_correct(n_int):
    print('Введено некорректное число')
    sys.exit()


sum_n = get_n_sum(n_str)
print('Сумма = ', sum_n)
