# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.


def fact(number):
    """
    Функция вычисляет факториал числа number
    Возвращает генератор
    :param number: число, факториал которого вычисляется
    :type number: int
    :return: генератор
    :type: generator
    """
    if number == 0:
        yield 1

    result = 1
    for n in range(1, number + 1):
        result *= n
        yield result


def main():
    """
    Основная функция
    Создает генератор с помощью функции, которая вычисляет фактриал числа
    Выводит факториалы чисел от 1 до заданного числа
    """
    for elem in fact(5):
        print(elem)


# Вызов основной функции
main()
