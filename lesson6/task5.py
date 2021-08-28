class Stationery:
    """ Класс, описывающий объект 'Канцелярская принадлежность' """
    def __init__(self, title):
        """
        Конструктор класса
        :param title: название объекта
        :type title: str
        """
        self.title = title

    def draw(self):
        """ Функция отрисовки """
        print('Запуск отрисовки')


class Pen(Stationery):
    """ Класс, описывающий объект 'Ручка' """
    def draw(self):
        print(f'{self.title} рисует как ручка')


class Pencil(Stationery):
    """ Класс, описывающий объект 'Карандаш' """
    def draw(self):
        print(f'{self.title} рисует как карандаш')


class Handle(Stationery):
    """ Класс, описывающий объект 'Маркер' """
    def draw(self):
        print(f'{self.title} рисует как маркер')


def main():
    """
    Основная функция
    Создает объекты некоторых классов, запускает отрисовку каждого созданного объекта
    """
    # Канцелярская принадлежность
    stationery = Stationery('Что-то')
    stationery.draw()

    # Ручка
    pen = Pen('Linc')
    pen.draw()

    # Карандаш
    pencil = Pencil('Maped')
    pencil.draw()

    # Маркер
    marker = Handle('Какой-то маркер')
    marker.draw()


main()
