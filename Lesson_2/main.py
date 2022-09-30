def words_counter(filename, dict):
    with open(filename, 'r', encoding='cp1251') as file:
        all_words = [w.strip().casefold() for w in file.read().split(' ')]
        for word in all_words:
            if word not in dict:
                dict[word] = {
                    'count': 0,
                    'doc': set()
                }
            dict[word]['count'] += 1
            dict[word]['doc'].add(hash(filename))
    return dict


def tf(dict):
    total_count = len(dict)
    tf_dictionary = {}
    for w, c in dict:
        tf_dictionary[w] = c['count'] / total_count
    return tf_dictionary


def idf(dict, tf_dict):
    tf_idf_dict = {}
    files = {}
    for k, v in dict:
        if v['doc'] not in files:
            files[v['doc']]


if __name__ == '__main__':
    dictionary = {}
    dictionary = words_counter('voyna-i-mir-tom-1.txt', dictionary)
    print(len(dictionary))
    dictionary = words_counter('Tolstoy Lev. Anna Karenina - BooksCafe.Net.txt', dictionary)
    print(len(dictionary))

    # print(dictionary)
