# Символ для вывода организации ячеек по рядам
symbol = '*'


def make_cells_order(cell, cells_count_in_row):
    """
    Обертка к функции make_order объекта cell
    Форматированный вывод
    :param cell: клетка
    :type cell: Cell
    :param cells_count_in_row: количество ячеек в одном ряду
    :type cells_count_in_row: int
    """
    print(f'{cells_count_in_row} ячеек в ряду:')
    print(cell.make_order(cells_count_in_row))


class Cell:
    """ Класс, описывающий объект клетки """
    def __init__(self, cells_count):
        self.cells_count = cells_count

    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        diff = self.cells_count - other.cells_count
        if diff < 0:
            print('Разность количества клеток меньше 0!')
            return Cell(0)
        return Cell(diff)

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        return Cell(round(self.cells_count / other.cells_count))

    def __str__(self):
        return str(self.cells_count)

    def make_order(self, cells_count_in_row):
        """
        Выводит ячейки по рядам
        Возвращает строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу
        :param cells_count_in_row: количество ячеек в одном ряду
        :type cells_count_in_row: int
        :return: строка вида *****\n*****\n*****...
        :rtype: str
        """
        if cells_count_in_row == 0:
            return ''

        # Результат целочисленного деления и остаток деления
        quotient, remainder = divmod(self.cells_count, cells_count_in_row)

        # Формируем список вида ['***', '***', '***'], где количество символов в строке = cells_count_in_row
        # количество элементов в списке = quotient
        parts = [symbol * cells_count_in_row] * quotient
        # Если не все ячейки поместились по рядам добавляем остаток
        if remainder != 0:
            parts += [symbol * remainder]

        return '\n'.join(parts)


def main():
    """
    Основная функция
    Создает объекты класса клетки
    Выводит результаты сложения, вычитания, умножения и деления клеток
    """
    c1 = Cell(3)
    c2 = Cell(5)

    print('Сложение:', c1 + c2)
    print('Умножение:', c1 * c2)
    print('Вычитание из первой клетки:', c1 - c2)
    print('Вычитание из второй клетки:', c2 - c1)
    print('Деление первой на вторую:', c1 / c2)
    print('Деление второй на первую:', c2 / c1)

    for c_idx, c in enumerate([c1, c2]):
        print(f'\nВывод ячеек {c_idx + 1}-ой клетки по рядам ({c.cells_count}):')
        for i in range(1, c.cells_count + 3):
            make_cells_order(c, i)


main()
