from operator import add
from random import randint


def get_rand_matrix(rows_count, cols_count):
    """
    Возвращает матрицу размерности rows_count x cols_count с рандомными элементами
    :param rows_count: количество строк
    :type rows_count: int
    :param cols_count: количество столбцов
    :type cols_count: int
    :rtype: Matrix
    """
    data = [[randint(0, 10) for _ in range(cols_count)] for _ in range(rows_count)]
    return Matrix(data)


def print_matrix_info(m):
    """
    Выводит саму матрицу и информцию о ней
    :param m: матрица
    :type m: Matrix
    """
    if m is None:
        return
    print(f'Матрица размером {m.rows_count}x{m.cols_count}:')
    print(f'{m}\n')


class Matrix:
    """ Класс, описывающий матрицу """

    def __init__(self, data=None):
        """
        Конструктор класса
        Если на входе - список списков разного размера, то в качестве содержимого матрицы устанавливается пустой
        список
        :param data: спписок списков чисел
        :type data: List[List[number]]
        """
        self.data = data if data is not None and len(set(map(len, data))) == 1 else []

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.is_dim_equal(other):
            data_sum = [list(map(add, self.data[i], other.data[i])) for i in range(self.rows_count)]
            return Matrix(data_sum)

    def is_dim_equal(self, other):
        """
        Сравнивает размерности с размерностями матрицы other
        :param other: матрица, с которой сраванивается
        :type other: Matrix
        :return: совпадают ли размерности
        :rtype: bool
        """
        return self.rows_count == other.rows_count and self.cols_count == other.cols_count

    @property
    def cols_count(self):
        """ Количество столбцов матрицы """
        return len(self.data[0]) if self.data else 0

    @property
    def rows_count(self):
        """ Количество строк матрицы """
        return len(self.data) if self.data else 0


def main():
    """
    Основная функция
    Создает несколько матриц, выводит их в консоль, выполняет сложение матриц
    """
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    print_matrix_info(m1)

    m2 = get_rand_matrix(2, 3)
    print_matrix_info(m2)

    print('Сумма матриц')
    print_matrix_info(m1 + m2)

    m3 = get_rand_matrix(3, 3)
    print_matrix_info(m3)

    print('Попытка сложить матрицы разных размерностей')
    print_matrix_info(m3 + m2)

    print('-' * 100)
    print('Пустая матрица')
    m4 = Matrix()
    print_matrix_info(m4)

    print('Некорректная матрица')
    m5 = Matrix([[1, 2, 3], [4, 5]])
    print_matrix_info(m5)


main()
