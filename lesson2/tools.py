# Вспомогательные функции


def convert_to_number(var_str, func=int):
    """
    Конвертация строки в число такого типа, определяемого функцией приведения func
    Если не сможет сконвертировать, вернет None
    :param var_str: значение, которое будет сконвертировано
    :type var_str: str
    :param func: функция приведения
    :type func: function
    :return: число
    :type: тип func
    """
    # Функция преобразования может быть не определена, в этом случае возвращается None
    if func is None:
        return None

    # Иначе пробуем сконвертировать в тип func
    try:
        return func(var_str)
    except ValueError:
        return None


def is_correct(var_num):
    """
    Проверка числа на корректность
    Число корректно, если оно > 0 и не None
    :param var_num: число, корректность которого проверяется
    :type var_num: int или float
    :return: показатель корректности числа
    :type: bool
    """
    # Нужны только положительные числа
    if var_num is None or var_num <= 0:
        return False
    return True
