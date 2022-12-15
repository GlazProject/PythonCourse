import math
import string
import re


def txt_file(filename: str) -> str:
    if not filename.endswith('.txt'):
        filename += '.txt'
    return filename


def write_in_dictionary(words_dictionary: dict, word: str, file_name: str):
    word = word.casefold().replace(' ', ' ')

    # Добавление нового слова или обновление количества в словарь
    if word not in words_dictionary:
        words_dictionary[word] = {
            'count': 0,
            'files': {}
        }
    words_dictionary[word]['count'] += 1

    # Обновление количества слов для конкретного файла
    file_hash = hash(file_name)
    if file_hash not in words_dictionary[word]['files']:
        words_dictionary[word]['files'][file_hash] = 0
    words_dictionary[word]['files'][file_hash] += 1


def create_dictionary_from_file(filename: str, initial_dictionary: dict = None) -> dict:
    # Инициализация параметров по умолчанию
    if initial_dictionary is None:
        initial_dictionary = {}

    # Получение данных из файла
    with open(txt_file(filename), 'r', encoding='cp1251') as file:
        text = file.read()

    # Составление словаря
    words = re.finditer(r"\b\w+-?\w+\b", text, re.MULTILINE)
    for matchNum, word in enumerate(words, start=1):
        write_in_dictionary(initial_dictionary, word.group(), filename)

    return initial_dictionary


def get_total_words_count(words_dictionary: dict) -> int:
    return sum(value['count'] for value in words_dictionary.values())


def get_documents_count(words_dictionary: dict) -> int:
    documents = set()
    for key, value in words_dictionary.items():
        for document_id, document_count in value['files'].items():
            documents.add(document_id)
    return len(documents)


def tf_idf(all_words_dictionary: dict) -> dict:
    words_count = get_total_words_count(all_words_dictionary)
    documents_count = get_documents_count(all_words_dictionary)
    tf_idf_dictionary = {}
    for word, data in all_words_dictionary.items():
        tf = data['count'] / words_count
        idf = math.log2(documents_count / len(data['files']))
        tf_idf_dictionary[word] = {
            'count': data['count'],
            'tf-idf': tf * idf,
            'files_count': len(data['files'])
        }
    return tf_idf_dictionary


def get_output(tf_idf_dictionary: dict) -> str:
    word_number = 0
    result = ''
    for word, data in tf_idf_dictionary.items():
        word_number += 1
        line = f'{word_number}) {word:<{27 - len(str(word_number))}}:\t' \
               f'tf-idf = {data["tf-idf"]:2.3e},' \
               f' встречается {data["count"]:>8} раза' \
               f' в {data["files_count"]:>2} файлах\n'
        result += line
    return result


def print_words_in_console(tf_idf_dictionary: dict):
    print(get_output(tf_idf_dictionary))


def print_words_in_file(tf_idf_dictionary: dict, filename: str):
    print('[INFO] Запись в файл... ')
    with open(txt_file(filename), 'w', encoding='utf8') as file:
        file.write(get_output(tf_idf_dictionary))


def read_files(filenames: list[str], words_dictionary: dict = None) -> dict:
    if words_dictionary is None:
        words_dictionary = {}
    for filename in filenames:
        words_dictionary = create_dictionary_from_file(filename, words_dictionary)
        print(f'[INFO] Обработан "{filename}"')
    return words_dictionary


def main():
    print('[INFO] Start')
    filenames_for_reading = [
        'voyna-i-mir-tom-1',
        'Tolstoy Lev. Anna Karenina - BooksCafe.Net.txt',
        'istoriya-gosudarstva-rossiyskogo-tom-1.txt',
        'Dostoevskiy Fedor. Prestuplenie i nakazanie - BooksCafe.Net.txt'
    ]

    dictionary = read_files(filenames_for_reading)
    handled_dictionary = tf_idf(dictionary)

    # print_words_in_console(handled_dictionary)
    print_words_in_file(handled_dictionary, 'dictionary.txt')
    print('OK')


if __name__ == '__main__':
    main()
