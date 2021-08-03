# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import time
import sys
from tools import convert_to_number, is_correct


def get_formatted_seconds_time(seconds):
    """
    Вариант 1 - с использованием библиотеки time
    Переводит время в секундах в строку вида: hh:mm:ss
    """
    return time.strftime('%H:%M:%S', time.gmtime(seconds))


def get_formatted_seconds_divmod(seconds):
    """
    Вариант 2 - с использованием функции divmod
    Переводит время в секундах в строку вида: hh:mm:ss
    """
    # Отбрасываем сутки, если есть
    seconds = seconds % (24 * 3600)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds))


# Количество секунд в виде строки
seconds_str = input('Введите время в секундах: ')
# Пробуем сконвертировать в целое число
seconds = convert_to_number(seconds_str)
if not is_correct(seconds):
    print('Введено некорректное значение времени в секундах')
    sys.exit()


# Вариант 1 - с использованием библиотеки time
print(get_formatted_seconds_time(seconds))

# Вариант 2 - с использованием функции divmod
print(get_formatted_seconds_divmod(seconds))
