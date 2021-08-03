# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

# Булева переменная
var_bool = True

print(var_bool)
print(type(var_bool))

# Булевы переменные можно конвертить в числа: True = 1, False = 0
print(int(var_bool))
print(int(False))

# В вещественные тоже можно
print(float(True))
print(float(False))

# None можно конвертировать в bool переменную
print(bool(None))

# Целочисленная переменная
var_int = 5

print(var_int)
print(type(var_int))
print(float(var_int))
print(str(var_int))

# Вещественная переменная
var_float = 3.0

print(var_float)
print(type(var_float))
print(int(var_float))
print(str(var_float))

print()

var = input('Введите число: ')

# Если ввести не число или пустую строку, то будет exception
# Если ввести числа со знаком +/-, то тоже нормально сконвертирует
# Если в качестве разделителя точка, во float сможет привести
print(float(var))
# Если ввести число с точкой, то в int не сможет привести
print(int(var))
# Любая строка конвертируется в True, даже если ввести 0, None или пустую строку
print(bool(var))
