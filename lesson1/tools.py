# Вспомогательные функции


def convert_to_number(var_str, func=int):
    """
    Конвертация строки в число такого типа, определяемого функцией приведения func
    Если не сможет сконвертировать, вернет None
    """
    try:
        return func(var_str)
    except ValueError:
        return None


def is_correct(var_int):
    """ Проверка числа на корректность """
    # Нужны только целые положительные числа
    if var_int is None or var_int <= 0:
        return False
    return True
