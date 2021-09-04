from tools import convert_to_number, quit_symbol


class NanError(Exception):
    """ Класс исключений, генерируемый, если было введено не число """
    pass


class NumbersStore:
    """ Класс, хранящий введенные пользователем числа """

    # Список чисел, введенных пользователем
    _numbers = []

    @staticmethod
    def add_number(number):
        """
        Добавляет number в список класса, если это число, а не None
        :param number: введенное пользователем число
        :type number: float
        """
        if number is None:
            raise NanError('Введенное значение не является числом!')

        NumbersStore._numbers.append(number)

    @staticmethod
    def prompt_numbers():
        """
        Запрашивает у пользователя числа в бесконечном цикле
        Если пользователь введет специальный символ остановки цикла, то цикл завершается
        """
        while True:
            # Введенная пользователем строка
            number_str = input(f'Введите число (для выхода введите {quit_symbol.upper()}): ')
            if number_str.lower() == quit_symbol:
                break

            # Пробуем сконвертировать во float число
            number = convert_to_number(number_str, float)
            try:
                # Если введенная строка - число, добавляем в список класса
                NumbersStore.add_number(number)
            except NanError as e:
                print(e)

    @staticmethod
    def print_numbers():
        """ Виводит в консоль список чисел, введеных пользователем """
        print('Список введенных чисел:', NumbersStore._numbers)


def main():
    """
    Основная функция
    Запрашивает у пользователя числа в бесконечном цикле, если было введено не число,
    то выводится соответствующее сообщение, при этом цикл не завершается
    Цикл завершается, если пользователь введет специальный символ остановки цикла
    После остановки цикла, выводится список введенных чисел
    """
    # Запрашиваем числа
    NumbersStore.prompt_numbers()
    # После остановки цикла, отображаем введенные числа
    NumbersStore.print_numbers()


main()
