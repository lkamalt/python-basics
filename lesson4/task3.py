# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.


def main():
    """
    Основная функция
    Генерирует список чисел в пределах от 20 до 240, кратные 20 или 21
    """
    result = [v for v in range(20, 241) if v % 20 == 0 or v % 21 == 0]
    print('Список чисел [20, 240], кратные 20 или 21: ', result)


# Вызов основной функции
main()
