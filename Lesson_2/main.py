import math


def write_in_dictionary(words_dictionary, word, file_name):
    word = word.casefold()

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


def create_dictionary_from_file(filename: str, initial_dictionary=None, separator=None):
    # Инициализация параметров по умолчанию
    if initial_dictionary is None:
        initial_dictionary = {}
    if separator is None:
        separator = ' .,;:{}[]()*&^%$#@!?<>|+=\"\'\n-'

    # Получение данных из файла
    with open(filename, 'r', encoding='cp1251') as file:
        text = file.read()

    # Составление словаря за линейный проход по тексту
    start_index = 0
    for i in range(len(text)):
        if (text[i] in separator) or (i == len(text)-1):
            word = text[start_index:i]
            if len(word) > 0:
                write_in_dictionary(initial_dictionary, word, filename)
            start_index = i+1

    return initial_dictionary


def get_total_words_count(words_dictionary):
    count = 0
    for key in words_dictionary:
        count += words_dictionary[key]['count']
    return count


def get_documents_count(words_dictionary):
    documents = set()
    for key, value in words_dictionary.items():
        for document_id, document_count in value['files'].items():
            documents.add(document_id)
    return len(documents)


def tf_idf(all_words_dictionary):
    words_count = get_total_words_count(all_words_dictionary)
    documents_count = get_documents_count(all_words_dictionary)
    tf_idf_dictionary = {}
    for word, data in all_words_dictionary.items():
        tf = data['count'] / words_count
        idf = math.log2(documents_count/len(data['files']))
        tf_idf_dictionary[word] = {
            'count': data['count'],
            'tf-idf': tf*idf,
            'files_count': len(data['files'])
        }
    return tf_idf_dictionary


def get_output(tf_idf_dictionary):
    word_number = 0
    result = ''
    for word, data in tf_idf_dictionary.items():
        word_number += 1
        line = f'{word_number}) {word:25}:\t' \
               f'tf-idf = {data["tf-idf"]:2.5},' \
               f' встречается {data["count"]:8} раза' \
               f' в {data["files_count"]:2} файлах\n'
        result += line
    return result


def print_words_in_console(tf_idf_dictionary):
    print(get_output(tf_idf_dictionary))


def print_words_in_file(tf_idf_dictionary, filename):
    with open(filename, 'w', encoding='utf8') as file:
        file.write(get_output(tf_idf_dictionary))


if __name__ == '__main__':
    dictionary = create_dictionary_from_file('voyna-i-mir-tom-1.txt')
    dictionary = create_dictionary_from_file('Tolstoy Lev. Anna Karenina - BooksCafe.Net.txt', dictionary)
    handled_dictionary = tf_idf(dictionary)
    # print_words_in_console(handled_dictionary)
    print_words_in_file(handled_dictionary, 'dictionary.txt')
    print('OK')
