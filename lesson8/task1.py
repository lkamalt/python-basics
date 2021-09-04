class Date:
    """ Класс, описывающий даты """

    # Разделитель чисел в строке с датой
    date_sep_symbol = '-'

    def __init__(self, day, month, year):
        """
        Конструктор класса
        :param day: число
        :type day: int
        :param month: месяц
        :type month: int
        :param year: год
        :type year: int
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'Дата {self.day:02}{Date.date_sep_symbol}{self.month:02}{Date.date_sep_symbol}{self.year}'

    @classmethod
    def get_date_from_str(cls, date_str):
        """
        Возвращает объект даты, сформированный из строки с датой date_str
        :param date_str: дата в виде строки
        :type date_str: str
        :rtype: Date
        """
        date_numbers = Date.get_numbers_from_str(date_str)
        return cls(*date_numbers)

    @staticmethod
    def is_date_correct(date_str):
        """
        Проводит валидацию даты, заданной в виде строки
        :param date_str: дата в виде строки
        :type date_str: str
        :return: корректна ли дата
        :rtype: bool
        """
        day, month, year = Date.get_numbers_from_str(date_str)
        return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000

    @staticmethod
    def get_numbers_from_str(date_str):
        """
        Извлекает из строки с датой число, месяц и год, преобразует их в числа
        :param date_str: дата в виде строки
        :type date_str: str
        :return: [число, месяц, год]
        :rtype: List[int]
        """
        date_numbers = date_str.split(Date.date_sep_symbol)
        return list(map(int, date_numbers))


def main():
    """
    Основная функция
    Создает объект даты, отображает различную информацию о созданном объекте
    """
    date_str1 = '05-09-2021'
    date_str2 = '05-15-2021'

    print(f'Новый объект класса {Date.__name__}:', Date.get_date_from_str(date_str1))

    print(f'Корректна ли дата {date_str1}? -', Date.is_date_correct(date_str1))
    print(f'Корректна ли дата {date_str2}? -', Date.is_date_correct(date_str2))


main()
