# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from tools import get_randint_list, write_data_to_file


def get_numbers_from_file(file_name):
    """
    Считывание списка целых чисел из файла
    :param file_name: название файла
    :type file_name: str
    :return: список целых чисел
    :type: List[int]
    """
    with open(file_name, 'r') as f:
        return [int(s) for s in f.read().split()]


def main():
    """
    Основная функция
    Генерирует список из целых рандомных чисел
    Записывает сгенерированный список в файл, числа разделяются пробелом
    Производится считывание списка чисел из этого файла
    """
    # Генерируем список из 10 рандомных чисел из диапазона [0, 20]
    numbers = get_randint_list(0, 20, 10)
    # Имя файла куда будут записаны числа
    file_name = 'task5.txt'

    # Записываем список в файл
    write_data_to_file(file_name, map(str, numbers))
    # Считываем эти числа из файла
    numbers = get_numbers_from_file(file_name)

    # Выводим список чисел и их сумму на экран, если удалось считать список из файла
    if numbers is not None:
        print('Сгенерированный список чисел:', numbers)
        print('Сумма чисел:', sum(numbers))


main()
