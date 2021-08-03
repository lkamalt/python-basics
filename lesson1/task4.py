# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

import sys
from tools import convert_to_number, is_correct


def get_max_digit_str_search(n_str):
    """ Вариант 1 - цикл по строке со сравнением с максимальным """
    # Первый символ строки, сконвертированный в число
    # Можно обратиться к первому элементу строки, потому что приходит уже корректное число
    n_max = int(n_str[0])

    for i in range(1, len(n_str)):
        n = int(n_str[i])
        if n > n_max:
            n_max = n

    return n_max


def get_max_digit_list(n_str):
    """ Вариант 2 - с использованием списков """
    l_int = [convert_to_number(l) for l in list(n_str)]
    return max([l for l in l_int if l is not None])


def get_max_digit_arith(n_int):
    """ Вариант 3 - с использованием while и арифметических операций %, // """
    res_div = n_int
    n_max = 0

    while res_div != 0:
        # res_div, res_mod = divmod(n_int, 10)

        res_mod = res_div % 10
        res_div //= 10

        if res_mod > n_max:
            n_max = res_mod

    return n_max


# Введенное число в виде строки
n_str = input('Введите целое положительное число: ')

# Пробуем сконвертировать
n_int = convert_to_number(n_str)

# Проверяем, что не None и > 0, иначе заврешаем программу
if not is_correct(n_int):
    print('Было введено некорректное число')
    sys.exit()


# После проверок в функции уже будет идти только строка ненулевой длины, содержащая целое, положительное число

# Вариант 1 - посимвольный цикл по строке со сравнением с максимальным ----------------------------
# Отправляем в функции именно str(int), потому что может быть введено число со знаком: +12345,
# а в функции анализируется строка посимвольно, начиная с первого
# Тут можно было еще использовать n_str.lstrip('+') вместо конвертации
n_max = get_max_digit_str_search(str(n_int))

# Вариант 2 - генерируем список из символов строки и конвертируем поэлементно в int ---------------
# Здесь можно отправить просто n_str, потому что внутри функции для конвертации используется
# кастомная функция, которая в случае чего вернет None, а его уже можно обработать
# n_max = get_max_digit_list(n_str)

# Вариант 3 - с использованием while и арифметических операций ------------------------------------
# n_max = get_max_digit_arith(n_int)

print('Самая большая цифра в введенном числе: ', n_max)