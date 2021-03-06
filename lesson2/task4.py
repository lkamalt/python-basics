#  Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.


def print_words(words):
    """
    Выводит слова в консоль с порядковым номером, начиная с 1
    Если слово длинное, выводит только первые 10 букв слова
    :param words: список слов, которые нужно вывести в консоль
    :type words: List[str]
    """
    for i, word, in enumerate(words):
        w = word if len(word) <= 10 else word[0:10]
        print(f'{i + 1}: {w}')


def main():
    """
    Основная функция
    Запрашивает у пользователя список слов через пробел
    Выводит в консоль слова с соответствующим порядковым номером, начиная с 1
    Если слово длинное, выводит только первые 10 символов слова
    """
    # Введенные слова в виде одной строки
    words_str = input('Введите несколько слов через пробел: ')

    # Разбиваем входную строку на список строк по пробелу
    words = words_str.split()

    # Выводим введенные слова в консоль по некоторым правилам
    print_words(words)


# Вызов основной функции
main()
