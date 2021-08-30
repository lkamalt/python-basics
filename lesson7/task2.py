from abc import ABC, abstractmethod


class Clothes(ABC):
    """ Класс, описывающий объект одежды """

    def __init__(self, title):
        """
        Конструктор класса
        :param title: название одежды
        :type title: str
        """
        self.__title = title

    @property
    def title(self):
        """ Название одежды """
        return self.__title

    @abstractmethod
    def get_total_expense(self):
        """
        Возвращает общий расход ткани
        :rtype: float
        """
        pass


class Coat(Clothes):
    """ Класс, описывающий объект 'Пальто' """

    def __init__(self, title, size):
        """
        Конструктор класса
        :param title: название пальто
        :type title: str
        :param size: размер пальто
        :type size: float
        """
        super().__init__(title)
        self.__size = size

    @property
    def size(self):
        """ Размер пальто """
        return self.__size

    def get_total_expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    """ Класс, описывающий объект 'Костюм' """

    def __init__(self, title, length):
        """
        Конструктор класса
        :param title: название костюма
        :type title: str
        :param length: высота костюма
        :type length: float
        """
        super().__init__(title)
        self.__length = length

    @property
    def length(self):
        """ Высота костюма """
        return self.__length

    def get_total_expense(self):
        return 2 * self.length + 0.3


def main():
    """
    Основная функция
    Создает объекты классов 'Пальто' и 'Костюм'
    Выводит информацию о созданных объектах
    """
    coat = Coat('Пальто', 80)
    suit = Suit('Костюм', 100)

    for cloth, attr in zip([coat, suit], ['size', 'length']):
        print(f'{cloth.title}: {getattr(cloth, attr)}\nОбщий расход ткани: {round(cloth.get_total_expense(), 2)}\n')


main()
