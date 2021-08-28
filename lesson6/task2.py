class Road:
    """ Класс, описывающий объект 'Дорога' """
    def __init__(self, length, width):
        """
        Конструктор класса
        :param length: длина дороги
        :param length: float
        :param width: ширина дороги
        :type width: float
        """
        self._length = length
        self._width = width

    def get_asphalt_mass(self, asph_mass_1sm, asph_thickness):
        """
        Вычисляет массу асфальта, необходимого для покрытия всего дорожного полотна
        :param asph_mass_1sm: масса асфальта для покрытия 1 м^2 дороги толщиной в 1 см
        :type asph_mass_1sm: float
        :param asph_thickness: толщина полотна в см
        :type asph_thickness: float
        :return: масса асфальта для покрытия дороги толщиной asph_thickness см
        :type: float
        """
        return self._length * self._width * asph_mass_1sm * asph_thickness


def main():
    """
    Основная функция
    Создает объект класса Road, вычисляет массу асфальта, необходимого для покрытия всего дорожного полотна
    созданного объекта
    """
    road = Road(20, 5000)
    total_asph_mass = road.get_asphalt_mass(25, 5)
    print(f'Масса асфальта = {total_asph_mass / 1000} т')


main()
