from enum import Enum


class OfficeEquipmentType(Enum):
    """ Перечисление: типы офисной техники """
    Printer = 'Принтер'
    Scanner = 'Сканер'
    Xerox = 'Ксерокс'


class DepartmentType(Enum):
    """ Перечисление: типы департаментов офиса """
    IT = 'IT'
    Design = 'Дизайн'
    Economics = 'Экономика'


# Список типов офисной техники
office_equipment_types = list(OfficeEquipmentType)
# Список подразделений
department_types = list(DepartmentType)


class OfficeEquipmentStore:
    """ Класс, описыващий склад офисного оборудования """

    # Словарь: тип данных - тест сообщения об ошибке
    # Используется в функции проверки типа значения
    _value_class_to_err_msg = {
        OfficeEquipmentType: 'Неизвестный тип оборудования!',
        DepartmentType: 'Неизвестный тип департамента!',
        int: 'Некорректный формат значения количества оборудования!'
    }

    def __init__(self):
        # Словарь количества техники на складе по типу: вид техники - общее количество на складе
        self._equip_type_to_count_store = {equip_type: 0 for equip_type in office_equipment_types}
        # Словарь количества техники по департаменту: департамент - {вид техники - общее количество}
        self._dep_type_to_count = {dep_type: {equip_type: 0 for equip_type in office_equipment_types}
                                   for dep_type in department_types}

    def __str__(self):
        # Количество символов, которое отводится на отображение названия и склада
        place = 10
        s1 = f'{"На складе":>{place}}: {self.get_str_from_dict(self._equip_type_to_count_store)}\n'
        s2 = '\n'.join([f'{n.value:>{place}}: {self.get_str_from_dict(d)}' for n, d in self._dep_type_to_count.items()])
        return s1 + s2

    @property
    def total_equipment_count(self):
        """
        Возвращает общее количество техники на складе и в департаментах
        :rtype: int
        """
        return self.store_equipment_count + self.departments_equipment_count

    @property
    def store_equipment_count(self):
        """
        Возвращает количество техники на складе
        :rtype: int
        """
        return sum(self._equip_type_to_count_store.values())

    @property
    def departments_equipment_count(self):
        """
        Возвращает количество техники, отданное в департаменты
        :rtype: int
        """
        return sum([sum(v.values()) for v in self._dep_type_to_count.values()])

    @property
    def equip_types(self):
        """
        Возвращает список типов оборудования на складе
        :rtype: List[OfficeEquipmentType]
        """
        return list(self._equip_type_to_count_store.keys())

    def receive_new_equipment(self, equip_type, equip_count):
        """
        Добавление нового оборудования на склад
        :param equip_type: тип оборудования
        :type equip_type: OfficeEquipmentType
        :param equip_count: количество оборудования
        :type equip_count: int
        """
        # Проверка, что переменная с количеством оборудования - целое число
        if not self.is_correct(equip_count, int):
            return

        # Проверка на корректность типа оборудования
        if not self.is_correct(equip_type, OfficeEquipmentType):
            return

        # Если такого оборудования еще нет не складе, создаем запись о нем в словаре
        if equip_type not in self._equip_type_to_count_store:
            self.add_new_equipment_type(equip_type)

        # Если заданный тип оборудования уже есть в списке известных, то увеличиваем количество этого оборудования
        self._equip_type_to_count_store[equip_type] += equip_count

    def transfer_equipment_to_department(self, dep_type, equip_type, equip_count):
        """
        Передача оборудования из склада в заданный департамент
        :param dep_type: департамент, куда отдается оборудование
        :type dep_type: DepartmentType
        :param equip_type: тип оборудования, которое передается департаменту
        :type equip_count: OfficeEquipmentType
        :param equip_count: количество техники, которое передается департаменту
        :type equip_count: int
        """
        # Проверка, что переменная с количеством оборудования - целое число
        if not self.is_correct(equip_count, int):
            return

        # Проверка на корректность типа департамента
        if not self.is_correct(dep_type, DepartmentType):
            return

        print(f'Запрос: {equip_count} единиц типа {equip_type.value} в департамент {dep_type.value}')

        # Если такого оборудования, которое мы хотим передать департаменту даже нет на складе, то выводим
        # сообщение о том, что сначала его надо добавить на склад
        if equip_type not in self._equip_type_to_count_store:
            print(f'Оборудования типа {equip_type.value} нет на складе. '
                  f'Отправка оборудования в департамент {dep_type.value} не будет произведена, '
                  f'необходимо сначала добавить оборудование на склад.')
            return

        # Общее количество техники типа equip_type на складе
        equip_count_store = self._equip_type_to_count_store[equip_type]
        if equip_count_store == 0:
            print(f'Оборудования типа {equip_type.value} нет складе. '
                  f'Отправка оборудования в департамент {dep_type.value} не будет произведена.')
            return

        # Если заданного департамента нет в списке учета, то создаем запись о нем в словаре
        if dep_type not in self._dep_type_to_count:
            self.add_new_department_type(dep_type)

        # Если количество товара на складе больше, чем требуемое, то департаменту отдается запрашиваемое количество
        # техники, иначе отдается столько сколько есть на складе
        if equip_count_store >= equip_count:
            result_equip_count = equip_count
        else:
            result_equip_count = equip_count_store
            print(f'На складе нет {equip_count} единиц оборудования типа {equip_type.value}. '
                  f'В департамент {dep_type.value} будет отправлено только {equip_count_store} единиц.')

        # Уменьшаем количество техники типа equip_type на складе
        self._equip_type_to_count_store[equip_type] -= result_equip_count
        # Увеличиваем количесто этой техники в нужном департаменте
        self._dep_type_to_count[dep_type][equip_type] += result_equip_count

    def get_equipment_count_by_department(self, dep_type, equip_type=None):
        """
        Возвращает общее количество оборудования (если None) в департаменте department_type
        Если equip_type задан, то возвращается количесто оборудования типа equip_type
        :param dep_type: тип департамента
        :type dep_type: DepartmentType
        :param equip_type: тип техники
        :type equip_type: OfficeEquipmentType
        :rtype: int
        """
        # Проверка корректности типа департамента и оборудования
        if not self.is_correct(dep_type, DepartmentType):
            return

        if dep_type in self._dep_type_to_count:
            if equip_type is None:
                return sum(self._dep_type_to_count[dep_type].values())
            elif self.is_correct(equip_type, OfficeEquipmentType):
                return self._dep_type_to_count[dep_type].get(equip_type)

    def get_equipment_count_in_store_by_type(self, equip_type):
        """
        Возвращает общее количество оборудования вида equip_type, которое есть на складе
        :param equip_type: тип оборудования
        :type equip_type: OfficeEquipmentType
        :rtype: int
        """
        # Проверка корректности типа оборудования
        if not self.is_correct(equip_type, OfficeEquipmentType):
            return

        return self._equip_type_to_count_store.get(equip_type)

    def add_new_equipment_type(self, equip_type):
        """
        Добавляет новый тип оборудования в учет склада
        :param equip_type: тип оборудования
        :type equip_type: OfficeEquipmentType
        :rtype: bool
        """
        self._add_new_type(equip_type, OfficeEquipmentType, 'оборудования')

    def add_new_department_type(self, dep_type):
        """
        Добавляет новый тип департамента в учет
        :param dep_type: тип департамента
        :type dep_type: DepartmentType
        :rtype: bool
        """
        self._add_new_type(dep_type, DepartmentType, 'департамента')

    def _add_new_type(self, value_type, ValueTypeClass, value_type_str):
        """
        Добавляет новый тип оборудования или департамента в учет
        :param value_type: тип объекта
        :type value_type: Union[OfficeEquipmentType, DepartmentType]
        :param ValueTypeClass: класс перечисления
        :type ValueTypeClass: Union[OfficeEquipmentType, DepartmentType]
        :param value_type_str: текст в сообщении
        :type value_type_str: str
        :rtype: bool
        """
        if ValueTypeClass == OfficeEquipmentType:
            # Для нового товара на складе
            self._equip_type_to_count_store[value_type] = 0
        else:
            # Для нового департамента
            self._dep_type_to_count[value_type] = {equip_type: 0 for equip_type in self.equip_types}

        # Выводим сообщение о добавлении нового типа
        print(f'Был добавлен новый тип {value_type_str}:', value_type.value)

    @staticmethod
    def is_correct(value, ValueClass):
        """
        Проверяет значение value на принадлежность к классу ValueClass
        :param value: проверяемое значение
        :type value: Union[OfficeEquipmentType, DepartmentType, int]
        :param ValueClass: класс, принадлежность к которому проеряется
        :rtype: bool
        """
        if not isinstance(value, ValueClass):
            print(OfficeEquipmentStore._value_class_to_err_msg[ValueClass])
            return False
        return True

    @staticmethod
    def get_str_from_dict(d):
        """
        Формирует строку из словаря в виде: key1: value1; key2: value2; ...
        :param d: словарь, значения которого объединяются в строку
        :type d: dict
        :rtype: str
        """
        return '; '.join([f'{k.value}: {v}' for k, v in d.items()])


class OfficeEquipment:
    """ Класс, описывающий офисное оборудование """

    def __init__(self, name, size):
        """
        Конструктор класса
        :param name: название техники
        :type name: str
        :param size: размер техники: длина, ширина, высота
        :type size: Tuple(float, float, float)
        """
        self.name = name
        self.size = size

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    """ Класс, описывающий объект 'Принтер' """

    def __init__(self, name, size, print_type, print_rate):
        """
        Конструктор класса
        :param name: название техники
        :type name: str
        :param size: размер техники: длина, ширина, высота
        :type size: Tuple(float, float, float)
        :param print_type: тип принтера
        :param print_rate: скорост печати
        :type print_rate: float
        """
        super().__init__(name, size)
        self.print_type = print_type
        self.print_rate = print_rate


class Scanner(OfficeEquipment):
    """ Класс, описывающий объект 'Сканер' """

    def __init__(self, name, size, scan_type, scan_area):
        """
        Конструктор класса
        :param name: название техники
        :type name: str
        :param size: размер техники: длина, ширина, высота
        :type size: Tuple(float, float, float)
        :param scan_type: тип сканера
        :param scan_area: площадь сканирования
        :type scan_area: float
        """
        super().__init__(name, size)
        self.scan_type = scan_type
        self.scan_area = scan_area


class Xerox(OfficeEquipment):
    """ Класс, описывающий объект 'Ксерокс' """

    def __init__(self, name, size, copy_rate, page_format):
        """
        Конструктор класса
        :param name: название техники
        :type name: str
        :param size: размер техники: длина, ширина, высота
        :type size: Tuple(float, float, float)
        :param copy_rate: скорость печати
        :type copy_rate: float
        :param page_format: формат страницы
        """
        super().__init__(name, size)
        self.copy_rate = copy_rate
        self.page_format = page_format


def main():
    """
    Основная функция
    Создает объект склада, производит наполнение склада техникой и перераспределяет технику по департаментам
    Выводит информацию о складе
    """
    def print_store():
        """ Функция форматированного вывода объекта склада """
        print(f'{store}\n')

    store = OfficeEquipmentStore()
    print('Начальное состояние склада')
    print_store()

    store.receive_new_equipment(OfficeEquipmentType.Printer, 10)
    store.receive_new_equipment(OfficeEquipmentType.Scanner, 5)
    store.receive_new_equipment(OfficeEquipmentType.Xerox, 2)
    print('Склад после наполнения')
    print_store()

    store.transfer_equipment_to_department(DepartmentType.IT, OfficeEquipmentType.Printer, 7)
    print_store()

    store.transfer_equipment_to_department(DepartmentType.Design, OfficeEquipmentType.Scanner, 10)
    print_store()

    store.transfer_equipment_to_department(DepartmentType.Economics, OfficeEquipmentType.Scanner, 5)
    print_store()

    print('Общее количество оборудования:', store.total_equipment_count)
    print('Количество оборудования на складе:', store.store_equipment_count)
    print('Количество оборудования в департаментах:', store.departments_equipment_count)

    print(f'Общее количество оборудования в департаменте {DepartmentType.IT.value}: '
          f'{store.get_equipment_count_by_department(DepartmentType.IT)}')

    printer = Printer('HP', (0.5, 0.5, 1), "Laser", 5)
    print('Принтер:', printer)


main()
