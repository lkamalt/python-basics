# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Параметры пользователя
fields = ('Имя', 'Фамилия', 'Год рождения', 'Город', 'Почта', 'Телефон')
# Значение параметров по умолчанию
def_value = ''


def print_person_data_dict(**person_data):
    """
    Выводит в консоль строку с данными пользователя
    :param person_data: словарь с данными пользователя
    :type person_data: dict
    """
    result = ''
    for p in person_data:
        result += f'{p}: {person_data[p]}; '
    print(result)


def print_person_data(name=def_value, surname=def_value, birth_year=def_value, city=def_value, email=def_value,
                      phone=def_value):
    """
    Выводит в консоль строку с данными пользователя
    :param name: имя
    :type name: str
    :param surname: фамилия
    :type surname: str
    :param birth_year: год рождения
    :type birth_year: str
    :param city: город проживания
    :type city: str
    :param email: почта
    :type email: str
    :param phone: телефон
    :type phone: str
    """
    print(f'Имя: {name}; Фамилия: {surname}; Год рождения: {birth_year} Город: {city}; Email: {email}; '
          f'Телефон: {phone};')


def get_person_data():
    """
    Запрашивает у пользователя данные по списку fields
    :return: словарь с данными пользователя
    :type: dict
    """
    person_info = {}
    for f in fields:
        person_info[f] = input(f'Введите значение поля "{f}": ')
    return person_info


def main():
    """
    Основная функция
    Запрашивает у пользователя данные: имя, фамилия, год рождения, город проживания, email, телефон
    Выводит данные пользователя в виде строки
    """
    # Заполняем словарь с данными пользователя
    person_data = get_person_data()

    # Вывод информации о пользователе
    # Вариант 1 - с использованием разыменования словаря
    print_person_data_dict(**person_data)
    # Вариант 2 - с именованными аргумментами
    print_person_data(name=person_data[fields[0]],
                      surname=person_data[fields[1]],
                      birth_year=person_data[fields[2]],
                      city=person_data[fields[3]],
                      email=person_data[fields[4]],
                      phone=person_data[fields[5]])


# Вызов основной функции
main()
