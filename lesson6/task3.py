class Worker:
    """ Класс, описывающий объект 'Работник' """
    def __init__(self, name, surname, position, wage, bonus):
        """
        Конструктор класса
        :param name: имя работника
        :type name: str
        :param surname: фамилия работника
        :type surname: str
        :param position: должность работника
        :type position: str
        :param wage: оклад
        :type wage: float
        :param bonus: премия
        :type bonus: float
        """
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position

        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    """ Класс, описывающий объект работника на некоторой должности """
    def get_full_name(self):
        """
        Возвращает полное имя сотрудника: имя фамилия
        :return: полное имя сотрудника
        :type: str
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        Возвращает величину дохода с учетом премии: оклад + премия
        :return: доход с учетом премии
        :type: float
        """
        return sum(self._income.values())


def main():
    """
    Основная функция
    Создает объект, описывающего работника с некоторой должностью
    Выводит информацию об этом сотруднике
    """
    programmer = Position('Кот', 'Матроскин', 'программист', 100000, 20000)
    print(f'Имя: {programmer.name}\nФамилия: {programmer.surname}\nДолжность: {programmer.position}\n')

    print('Полное имя:', programmer.get_full_name())
    print('Доход с учетом премии:', programmer.get_total_income())


main()
