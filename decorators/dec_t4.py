# Напишите декоратор retry:
#
# декоратор вызовает функцию, которая возвращает True/False для индикации успешного или неуспешного выполнения функции.
# При сбое декоратор должен подождать и повторить попытку выполнения функции.
# При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой.
# Если у декоратора заканчиваются попытки, он сдается и возвращает исключение
import time


def retry(func):
    def success(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    def wrapper(*args, **kwargs):
        attempts = 5
        sleep_ratio = 300
        for attempt in range(attempts):
            is_success, result = success(*args, **kwargs)
            if is_success:
                return result
            elif attempt == attempts-1:
                raise result
            print(f'[-] attempt {attempt+1} by {func.__name__} was failed. Wait {(attempt+1)*sleep_ratio}ms')
            time.sleep(((attempt+1)*sleep_ratio)/1000)
    return wrapper


@retry
def bad_func():
    return 4/0


@retry
def good_func():
    return 5/2


print(f'Значение хорошей функции: {good_func()}')
print(f'Значение плохой функции: {bad_func()}')
