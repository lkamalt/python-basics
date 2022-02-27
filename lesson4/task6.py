# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle
from tools import get_randint_list

# Максимальное число итераций для count и cycle
max_it_count = 20


def create_iterator(it_func, param):
    """
    Создает итератор с помощью функции it_func с параметром param
    Выводит числа max_it_count раз
    :param it_func: итератор
    :type it_func: Iterator
    :param param: параметр итератора: стартовое значение генерации чисел (для count)
                    или список, из которого будут браться числа для повтора (для cycle)
    :type param: int или List[int]
    """
    print(f'Использование {it_func.__name__}:')

    it_count = 0
    for v in it_func(param):
        if it_count > max_it_count:
            break

        # Выводим числа в одну строку
        print(v, end=' ')
        it_count += 1

    print()


def create_count_iterator(start):
    """
    Создает итератор, генерирующий целые числа, начиная со значения start
    Числа выводятся max_it_count раз
    :param start: начальное значение итератора
    :type start: int
    """
    create_iterator(count, start)


def create_cycle_iterator(arr):
    """
    Создает итератор, повторяющий элементы списка arr
    Числа выводятся max_it_count раз
    :param arr: список целых чисел
    :type arr: List[int]
    """
    create_iterator(cycle, arr)


def main():
    """
    Основная функция
    Создает два итератора: 1) генерирующий целые числа, начиная с указанного; 2) повторяющий элементы
    заранее заданного списка
    """
    # Создает итератор, генерирующий целые числа, начиная с указанного
    create_count_iterator(5)

    # Массив из 50 случайных целых чисел в диапазоне [0, 20]
    arr = get_randint_list(0, 20, 50)
    # Создает итератор, повторяющий элементы списка arr
    create_cycle_iterator(arr)


# Вызов основной функции
main()
