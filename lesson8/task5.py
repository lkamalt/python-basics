import numpy as np
from operator import add, sub, mul, truediv
from prettytable import PrettyTable

# Словарь: математическая операция - знак операции в виде строки
math_op_to_sign = {
    add: '+',
    sub: '-',
    mul: '*',
    truediv: '/'
}


class Complex:
    """ Класс, описывающий комплексные числа """

    # Символ мнимой единицы
    imag_unit_symbol = 'j'

    def __init__(self, real=0, imag=0):
        """
        Конструктор класса
        :param real: действительная часть
        :type real: float
        :param imag: мнимая часть
        :type imag: float
        """
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return Complex(real, imag)

    def __truediv__(self, other):
        try:
            denom = other.real * other.real + other.imag * other.imag
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real, imag)
        except ZeroDivisionError as e:
            print('Деление комплексного числа на 0:', e)

    def __abs__(self):
        return np.sqrt(self.real * self.real + self.imag * self.imag)

    def __str__(self):
        if np.isclose(self.data, 0).all():
            return '0'

        return self.real_str + self.sign_str + self.imag_str

    @property
    def real_str(self):
        """
        Возвращает действительную часть в виде строки
        Если действительная часть = 0, то вернет пустую строку
        :rtype: str
        """
        if np.isclose(self.real, 0):
            return ''
        return str(self.real)

    @property
    def imag_str(self):
        """
        Возвращает модуль мнимой части в виде строки + смивол мнимой единицы, например, 2j
        Если мнимая часть = 0, вернет пустую строку
        Если модуль мнимой части = 1, то вернет просто символ мнимаой единицы, например, j
        :rtype: str
        """
        if np.isclose(self.imag, 0):
            return ''

        # Модуль мнимой части
        image_abs = abs(self.imag)
        if np.isclose(image_abs, 1):
            return self.imag_unit_symbol

        return str(image_abs) + self.imag_unit_symbol

    @property
    def sign_str(self):
        """
        Возвращает знак мнимой части в виде строки
        Если действительная или мнимая часть = 0, то вернет пустую строку
        :rtype: str
        """
        if np.isclose(self.data, 0).any():
            return ''
        return '+' if self.imag > 0 else '-'

    @property
    def data(self):
        """
        Возвращает действительную и мнимую часть в виде списка
        :rtype: List[float]
        """
        return [self.real, self.imag]


def get_math_op_operands(c1, c2, math_op):
    """
    Возвращает строку, содержащую операнды и знак математической операции
    :param c1: первый операнд
    :type c1: Complex
    :param c2: второй операнд
    :type c2: Complex
    :param math_op: математическая операция
    :rtype: str
    """
    return f'({c1}) {math_op_to_sign[math_op]} ({c2})'


def main():
    """
    Основная функция
    Создает кастомные и встроенные комплексные числа
    Выводит значения модуля каждого числа в таблице
    Выполняет сложение, вычитание, умножение и деление кастомных и встроенных чисел, результат выводит в таблице
    """
    # Создание комплексных чисел ------------------------------------------------------------------
    # Список для кастомных комплексных чисел
    custom_complex = []
    # Список для встроенных комплексных чисел
    python_complex = []

    # Список составляющих для формирования комплексных чисел
    complex_parts = [(3, 2), (3, -2), (5, 1), (0, 2), (2, 0), (-8, 3), (0, 0), (-8, 0)]
    for parts in complex_parts:
        custom_complex.append(Complex(*parts))
        python_complex.append(complex(*parts))

    # Вывод таблицы модулей комплексных чисел -----------------------------------------------------
    # Формируем таблицу для вывода чисел и их модулей
    table_abs = PrettyTable()
    # Заголовок таблицы
    table_abs.field_names = ['Custom complex', 'Python complex', 'Custom abs', 'Python abs']
    # Количество знаков после запятой для округления
    round_digit = 2

    # Добавляем строки: кастомное число, встроенное число, модуль кастомного, модуль встроенного
    # Модули округляем до двух знаков после запятой
    for c, cp in zip(custom_complex, python_complex):
        table_abs.add_row([c, cp, round(abs(c), round_digit), round(abs(cp), round_digit)])

    print(table_abs)

    # Вывод таблицы математических операций с комплексными числами --------------------------------
    math_ops = [('Сложение', add), ('Вычитание', sub), ('Умножение', mul), ('Деление', truediv)]
    for name, op in math_ops:
        # Таблица для сравнения математических операция кастомных и встроенных комплексных чисел
        table_math_op = PrettyTable()
        # Заголовок таблицы
        table_math_op.field_names = ['Operands', 'Custom complex', 'Python complex']

        # Первый операнд - первое число в списке
        custom_v1 = custom_complex[0]
        python_v1 = python_complex[0]

        try:
            # Добавляем строки: строка с операндами, результат для кастомных чисел, результат дял встроенных чисел
            for i in range(1, len(custom_complex)):
                table_math_op.add_row([
                    get_math_op_operands(custom_v1, custom_complex[i], op),
                    op(custom_v1, custom_complex[i]),
                    op(python_v1, python_complex[i])])
        except ZeroDivisionError as e:
            print(f'Деление комплексного числа на 0 на итерации {i}:', e)

        print(name)
        print(table_math_op)


main()
