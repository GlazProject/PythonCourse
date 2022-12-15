#Готово

import functools
import random

from typing import List


# Модифицируйте код декоратора reverse_string
def reverse_string(func):
    """Если результат функции - строка, то ее нужно перевернуть. Иначе вернуть None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            return ''.join([result[i] for i in range(len(result)-1, -1, -1)])
        return None

    return wrapper


@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year():
    return 1957


# вывод для примера
print(
    get_university_name(),
    get_university_founding_year(),
    sep="\n"
)
