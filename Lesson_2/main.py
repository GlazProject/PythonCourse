def words_counter(filename, initial_dictionary=None):
    if initial_dictionary is None:
        initial_dictionary = {}
    with open(filename, 'r', encoding='cp1251') as file:
        # TODO Изменить проход по файлу и формирование словаря в линейный поиск
        all_words = [w.strip().casefold() for w in file.read().split(' ')]
        for word in all_words:
            if word not in initial_dictionary:
                initial_dictionary[word] = {
                    'count': 0,
                    'doc': set()
                }
            initial_dictionary[word]['count'] += 1
            initial_dictionary[word]['doc'].add(hash(filename))
    return initial_dictionary


def tf_idf(all_words_dictionary):
    total_count = len(all_words_dictionary)
    tf_dictionary = {}
    for w, c in all_words_dictionary:
        tf_dictionary[w] = c['count'] / total_count
    # TODO Написать алгоритм idf
    return tf_dictionary


if __name__ == '__main__':
    dictionary = words_counter('voyna-i-mir-tom-1.txt')
    print(len(dictionary))
    dictionary = words_counter('Tolstoy Lev. Anna Karenina - BooksCafe.Net.txt', dictionary)
    print(len(dictionary))
    # TODO Написать вызов функций составления idf словаря
    # TODO Написать функцию для красивого вывода словаря в консоль
