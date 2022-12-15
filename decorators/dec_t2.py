#Готово

import functools
import math
import random

from typing import List


# Модифицируйте код декоратора prime_filter
def prime_filter(func):
    def is_prime(x):
        if x == 2:
            return True
        for i in range(2, math.ceil(x**0.5)+1):
            if x % i == 0:
                return False
        return True

    """Дан список целых чисел, возвращайте только простые целые числа"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return [x for x in func(*args, **kwargs) if is_prime(x)]

    return wrapper


@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]


# вывод для примера
print(numbers(from_num=2, to_num=20))
