from enum import Enum


class Direction(Enum):
    """ Перечисление: направления поворота """
    Left = 0
    Right = 1
    Back = 2


class Car:
    """ Класс, описывающий объект 'Машина' """

    # Максимальная допустимая скорость машины
    max_speed = None

    def __init__(self, speed, color, name, is_police=False):
        """
        Конструктор класса
        :param speed: скорость
        :type speed: float
        :param color: цвет машины
        :type color: str
        :param name: название машины
        :type name: str
        :param is_police: яявляется машина полицейской
        :type is_police: bool
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """ Запуска машины """
        print(f'{self.name} поехала')

    def stop(self):
        """ Остановка машины """
        print(f'{self.name} остановилась')

    def turn(self, direction):
        """
        Поворот машины
        :param direction: направление поворота машины
        :type direction: Direction
        """
        if direction == Direction.Back:
            print(f'{self.name} развернулась')
        elif direction in [Direction.Left, Direction.Right]:
            direction_name = 'налево' if direction == Direction.Left else 'направо'
            print(f'{self.name} повернула {direction_name}')
        else:
            print(f'Неизвестное направление! {self.name} повернула непонятно куда')

    def show_speed(self):
        """
        Отображает текущую скорость машины
        В случае превышения скорости выводит дополнительное сообщение (если максимальная скорость задана)
        """
        msg = f'Скорость {self.name} = {self.speed} км/ч'

        # Если для некоторого класса задана максимальная скорость и текущая скорость машины
        # первышает максимальную, то выводится дополнительное сообщение о превышении
        if self.max_speed is not None and self.speed > self.max_speed:
            msg += f' - превышение скорости! Максимальная допустимая скорость: {self.max_speed} км/ч'

        print(msg)


class TownCar(Car):
    """ Класс, описывающий объект 'Городская машина' """
    # Задаем максимальную скорость для класса городских машин
    max_speed = 60


class SportCar(Car):
    """ Класс, описывающий объект 'Спортивная машина' """


class WorkCar(Car):
    """ Класс, описывающий объект 'Рабочая машина' """
    # Задаем максимальную скорость для класса рабочих машин
    max_speed = 40


class PoliceCar(Car):
    """ Класс, описывающий объект 'Полицейская машина' """


def show_car_methods_result(car, direction):
    """
    Вызывает все методы объекта car
    :param car: объект 'Машина'
    :param direction: направление поворота
    :type direction: Direction
    """
    car.go()
    car.show_speed()
    car.turn(direction)
    car.stop()
    print()


def show_car_properties(car):
    """
    Выводит в консоль все атрибуты машины
    :param car: объект 'Машина'
    """
    is_police = 'да' if car.is_police else 'нет'
    print(f'Название: {car.name}, скорость: {car.speed} км/ч, цвет: {car.color}, полицейская: {is_police}')


def main():
    """
    Основная функция
    Создает несколько объектов класса машины
    Выводит информацию о созданных машиных
    """
    # Объект общего класса
    car = Car(60, 'синий', 'BMW', False)
    show_car_properties(car)
    show_car_methods_result(car, Direction.Right)

    # Городская машина
    town_car = TownCar(80, 'белый', 'Lexus')
    show_car_properties(town_car)
    show_car_methods_result(town_car, Direction.Back)

    # Городская машина
    town_car = TownCar(50, 'белый', 'Toyota')
    show_car_properties(town_car)
    show_car_methods_result(town_car, Direction.Left)

    # Спортивная машина
    sport_car = SportCar(350, 'красный', 'Ferrari')
    show_car_properties(sport_car)
    show_car_methods_result(sport_car, Direction.Right)

    # Рабочая машина
    work_car = WorkCar(30, 'серебристый', 'ВАЗ')
    show_car_properties(work_car)
    show_car_methods_result(work_car, 0)

    # Рабочая машина
    work_car = WorkCar(50, 'серебристый', 'Ford')
    show_car_properties(work_car)
    show_car_methods_result(work_car, Direction.Back)

    # Полицейская машина
    police_car = PoliceCar(60, 'синий', 'Volkswagen', True)
    show_car_properties(police_car)
    show_car_methods_result(police_car, Direction.Left)


main()
