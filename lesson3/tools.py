# Вспомогательные функции

quit_symbol = 'q'


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
    except ValueError as e:
        # print(f'Не удалось сконвертировать в число: {e}\n')
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
