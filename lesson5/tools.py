# Вспомогательные функции

from operator import le
from random import randint
import json

# Специальный символ выхода из цикла запроса данных у пользователя
quit_symbol = 'q'


def convert_to_number(var_str, func=int, undef_value=None):
    """
    Конвертация строки в число такого типа, определяемого функцией приведения func
    Если не сможет сконвертировать, вернет None
    :param var_str: значение, которое будет сконвертировано
    :type var_str: str
    :param func: функция приведения
    :type func: function
    :param undef_value: выходное значение, если не удалось сконвертировать
    :return: число
    :type: тип func
    """
    # Функция преобразования может быть не определена, в этом случае возвращается None
    if func is None:
        return undef_value

    # Иначе пробуем сконвертировать в тип func
    try:
        return func(var_str)
    except ValueError as e:
        # print(f'Не удалось сконвертировать в число: {e}\n')
        return undef_value


def is_correct(var_num, compare=le):
    """
    Проверка числа на корректность
    Число корректно, если оно > 0 и не None
    :param var_num: число, корректность которого проверяется
    :type var_num: int или float
    :param compare: функция сравнения
    :type compare: function
    :return: показатель корректности числа
    :type: bool
    """
    # Нужны только числа, удовлетворяющие условию compare
    if var_num is None or compare(var_num, 0):
        return False
    return True


def get_number(msg, convert_func, condition=lambda x: True):
    """
    Запрашивает у пользователя число
    :param msg: сообщение для пользователя
    :type msg: str
    :param convert_func: функция приведения
    :type convert_func: function
    :param condition: дополнительное условие проверки
    :type condition: function
    :return: число, введенное пользователем
    :type: convert_func
    """
    while True:
        # Запрашиваем строку
        val_str = input(msg)
        if val_str.lower() == quit_symbol:
            return

        # Пробуем сконвертировать в число
        val = convert_to_number(val_str, convert_func)

        # Если получилось сконвертировать в число и число удовлетворяет условию condition,
        # то выходим из бесконечного цикла
        if val is not None and condition(val):
            return val


def get_randint_list(min_value, max_value, count):
    """
    Генерирует список целых чисел из интервала [start, stop]
    :param min_value: начало интервала, откуда берутся случайные числа
    :type min_value: int
    :param max_value: конец интервала, откуда берутся случайные числа
    :type max_value: int
    :param count: количество случайных чисел
    :type count: int
    :return: список случайных целых чисел
    :type: List[int]
    """
    return [randint(min_value, max_value) for i in range(count)]


def get_data_from_file(file_name):
    """
    Считывает данные из файла
    :param file_name: название файла
    :type file_name: str
    :return: список строк из файла
    :type: List[str]
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.readlines()


def write_data_to_file(file_name, data, sep=' '):
    """
    Запись списка строк в файл
    :param file_name: название файла
    :type file_name: str
    :param data: список строк, которые будут записаны в файл
    :type data: List[str]
    :param sep: разделитель слов в файле, с которым будут записаны элементы списка data
    :type sep: str
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(sep.join(data))


def serialize_data_json(file_name, data):
    """
    Запись данных в json
    :param file_name: название json-файла
    :type file_name: str
    :param data: данные для записи в json
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def deserialize_data_json(file_name):
    """
    Извлечение данных из json
    :param file_name: название json-файла
    :type file_name: str
    :return: считанные данные
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)
