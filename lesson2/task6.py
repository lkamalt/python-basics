# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

from collections import defaultdict
from tools import convert_to_number


# Названия полей - характеристик каждого товара
fields = ('название', 'цена', 'количество', 'ед')
# Самое длинное название поля (нужно для красивого отображения аналитики)
max_len = max([len(w) for w in fields])

# Функции приведения для каждого поля, функции преобразования есть только у числовых полей
convert_funcs = [None, float, int, None]


def print_menu():
    """ Отображает меню на экране """
    print('\n1 - Внести данные товара\n2 - Вывести список всех товаров\n3 - Вывести аналитику по товарам\n4 - Выход')


def print_all_items(items):
    """
    Выводит на консоль информацию о каждом товаре
    :param items: список кортежей вида (idx, item), где
                    idx - номер товара,
                    item - товар в виде словаря {f: field_value for f in fields}
    :type items: List[tuple(int, dict)]
    """
    for item in items:
        print(item)


def get_new_item():
    """
    Создает товар в виде словаря, ключи словаря из кортежа fields, значения полей вводит пользователь
    :return: объект товара в виде словаря: {f: field_value for f in fields}
    :type: dict
    """
    item = {}
    for i, field in enumerate(fields):
        # Значение поля в виде строки
        field_value = input(f'Введите значение поля {field}: ')
        # Если это числовое поле, то пробуем сконвертировать
        field_value_convert = convert_to_number(field_value, convert_funcs[i])
        # Если поле строковое, оставляем строку
        # Если удалось привести к числу, то заносим в словарь это число, иначе, оставляем строку
        item[field] = field_value_convert if field_value_convert else field_value
    return item


def get_analytics(items):
    """
    Собирает аналитику всех товаров в словарь
    :param items: список кортежей вида (idx, item), где
                    idx - номер товара,
                    item - товар в виде словаря {f: field_value for f in fields}
    :type items: List[tuple(int, dict)]
    :return: аналитика товаров в виде словаря: {f: [field_value1, field_value2, ...] for f in fields}
    :type: dict
    """
    # Словарь с аналитикой: поле - список значений поля
    an_data = defaultdict(list)

    # Пробегаемся по всем товарам и собираем значения поля каждого товара в список
    for item in items:
        for field, field_value in item[1].items():
            an_data[field].append(field_value)

    return an_data


def print_analytics(an_data):
    """
    Отображает аналитику о товарах: список всех названий, цен, количеств и т. д.:
    :param an_data: словарь с аналитикой товаров вида: {f: [field_value1, field_value2, ...] for f in fields}
    :type an_data: dict
    """
    # При выводе отводим для названия поля
    # максимальное количество символов (= самое длинное название поля) + 2 (число 2 - произвольно)
    for field, field_data in an_data.items():
        print(f'{field:{max_len + 2}} {field_data}')


def main():
    """
    Основная функция
    Отображатет пользователю меню с вариантами работы
    Есть возможность формирования списка товаров, отображения всего списка и аналитики товаров
    """
    # Список всех товаров - список кортежей вида: [(idx1, item1), (idx2, item2), ...],
    # idx - номер товара (начинается с 1), item - словарь с характеристиками товара
    items = []
    # Общее количество товаров
    items_count = 0

    while True:
        # Вывод меню
        print_menu()
        # Запрашиваем у пользователя дальнейшее действие
        choice = input('Введите пункт меню: ')

        if choice == '1':
            # Так как было выбрано добавление товара, то увеличиваем общее количество товаров
            items_count += 1

            print(f'Ввод данных товара №{items_count}')
            # Создаем новый товар, объект товара представляет собой словарь с его данными
            item = get_new_item()
            # Добавляем в список товаров кортеж с товаром и его номером
            items.append((items_count, item))

        elif choice == '2':
            print('Информация по всем товарам:')
            print_all_items(items)

        elif choice == '3':
            print('Аналитика о товарах:')
            print_analytics(get_analytics(items))

        elif choice == '4':
            print('Выход из программы')
            break

        else:
            print('Введите правильный пункт меню: 1, 2, 3, 4')


# Вызов основной функции
main()
