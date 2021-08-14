# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

from tools import convert_to_number, is_correct


# Простая реализация перечисления для названий времен года
# Благодаря этому можно легко поменять способ отображения названия, например, перевести названия на английский
class Season:
    Winter = 'Зима'
    Spring = 'Весна'
    Summer = 'Лето'
    Autumn = 'Осень'


# Словарь: номер месяца - время года
month_idx_to_season = {
    1: Season.Winter,
    2: Season.Winter,
    3: Season.Spring,
    4: Season.Spring,
    5: Season.Spring,
    6: Season.Summer,
    7: Season.Summer,
    8: Season.Summer,
    9: Season.Autumn,
    10: Season.Autumn,
    11: Season.Autumn,
    12: Season.Winter,
}

# Словарь: время года - список соответствующих номеров месяца
season_to_month_idxs = {
    Season.Winter: [1, 2, 12],
    Season.Spring: [3, 4, 5],
    Season.Summer: [6, 7, 8],
    Season.Autumn: [9, 10, 11]
}

# Список времен года по месяцам
seasons = [Season.Winter, Season.Winter,
           Season.Spring, Season.Spring, Season.Spring,
           Season.Summer, Season.Summer, Season.Summer,
           Season.Autumn, Season.Autumn, Season.Autumn,
           Season.Winter]

# Можно еще так)
# seasons = [Season.Winter] * 2 + [Season.Spring] * 3 + [Season.Summer] * 3 + [Season.Autumn] * 3 + [Season.Winter]


def get_season_by_month_idx_dict(month_idx):
    """
    По номеру месяца возвращает соответствующее время года
    Функция с использованием словаря month_idx_to_season
    :param month_idx: номер месяца
    :type month_idx: int
    :return: название времени года
    :type: str
    """
    # В эту функцию идут уже корректные данные, поэтому обработка случая отсутствия ключа в словаре не нужна
    return month_idx_to_season[month_idx]


def get_season_by_month_idx_dict_list(month_idx):
    """
    По номеру месяца возвращает соответствующее время года
    Функция с использованием словаря season_to_month_idxs
    :param month_idx: номер месяца
    :type month_idx: int
    :return: название времени года
    :type: str
    """
    for season, month_idxs in season_to_month_idxs.items():
        if month_idx in month_idxs:
            return season


def get_season_by_month_idx_list(month_idx):
    """
    По номеру месяца возвращает соответствующее время года
    Функция с использованием списка seasons
    :param month_idx: номер месяца
    :type month_idx: int
    :return: название времени года
    :type: str
    """
    # Так как нумерация месяцев идет с 1, то при обращении к элементам списка нужно из номера month_idx вычесть 1
    return seasons[month_idx - 1]


def main():
    """
    Основная функция
    Запрашивает у пользователя номер месяца
    По введенному номеру месяца выводится соответствующее название времени года
    Используются вызовы функций с разными способами определения
    """
    # Номер месяца в виде строки
    month_idx_str = input('Введите номер месяца: ')
    # Пробуем сконвертировать в интовое число
    month_idx = convert_to_number(month_idx_str)

    # Нужно число, удовлетворяющее условию: 0 < month_idx <= 12
    if not is_correct(month_idx) or month_idx > 12:
        print('Введен некорректный номер месяца')
        return

    # Вариант 1 - с использование словаря month_idx_to_season
    season = get_season_by_month_idx_dict(month_idx)

    # Вариант 2 - с использование словаря season_to_month_idxs
    # season = get_season_by_month_idx_dict_list(month_idx)

    # Вариант 3 - с использование списка seasons
    # season = get_season_by_month_idx_list(month_idx)

    print(f'Месяц с номером {month_idx} соответствует времени года: {season}')


# Вызов основной функции
main()
