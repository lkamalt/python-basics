# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

from tools import get_data_from_file


def get_words_count(data):
    """
    Возвращает список из числа слов в каждом элементе списка data
    Считается, что слова в каждом элементе списка data разделены пробелом
    Каждый элемент списка data является строкой
    :param data: список строк
    :type data List[str]
    :return: список из числа слов в каждой строке
    :type: List[int]
    """
    return [len(d.split()) for d in data]


def main():
    """
    Основная функция
    Выводит информацию о содержимом файла: количество строк в файле, количество слов в каждой строке файла
    Слова в файле считаются отдельными, если они разделены пробелами
    """
    # Список строк из файла
    data = get_data_from_file('task2.txt')
    # Количество слов в каждой строке из файла
    words_count_by_row = get_words_count(data)

    print('Общее количество строк в файле: ', len(data))
    for row_idx, words_count in enumerate(words_count_by_row):
        print(f'Количество слов в строке {row_idx + 1}: {words_count}')


main()
