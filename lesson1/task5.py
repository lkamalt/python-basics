# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

import sys
from tools import convert_to_number, is_correct

proceeds_str = input('Введите значение выручки: ')
proceeds = convert_to_number(proceeds_str, float)
if not is_correct(proceeds):
    print('Введено некорректное значение выручки')
    sys.exit()

costs_str = input('Введите значение издержек: ')
costs = convert_to_number(costs_str, float)
if not is_correct(costs):
    print('Введено некорректное значение издержек')
    sys.exit()


if proceeds > costs:
    print('Компания отработала с прибылью')

    # Расчет прибыли: выручка - издержки
    profit = proceeds - costs
    print(f'Прибыль компании = {profit:.2f}')

    # Расчет рентабельности: прибыль / выручка
    profitability = profit / proceeds
    print(f'Рентабельность компании = {profitability:.2f}')

    employees_count_str = input('Введите количество сотрудников: ')
    employees_count = convert_to_number(employees_count_str)
    if not is_correct(employees_count):
        print('Введено некорректное число сотрудников')
        sys.exit()

    # Расчет удельной прибыли - прибыли на 1 сотрудника: прибыль / количество_сотрудников
    spec_profit = profit / employees_count
    print(f'Прибыль фирмы в расчете на 1 сотрудника = {spec_profit:.2f}')
else:
    print('Компания отработала с убытком')
