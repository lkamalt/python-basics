# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

import sys
from tools import convert_to_number, is_correct

init_dist_str = input('Введите результат пробежки за первый день (км): ')
init_dist = convert_to_number(init_dist_str, float)
if not is_correct(init_dist):
    print('Введено некорректное значение результата пробежки за первый день')
    sys.exit()


target_dist_str = input('Введите необходимое расстояние (км): ')
target_dist = convert_to_number(target_dist_str, float)
if not is_correct(target_dist):
    print('Введено некорректное значение необходимого расстояния')
    sys.exit()


# Номер дня
day_idx = 1
while init_dist < target_dist:
    # Выводим промежуточный результат
    print(f'Результат за {day_idx} день: {init_dist:.2f} км')
    # Общий результат будем накапливать в переменной init_dist
    init_dist += init_dist * 0.1
    day_idx += 1

# Вывод результата
print(f'На {day_idx} день общий результат спортсмена составит {init_dist:.2f} км')
