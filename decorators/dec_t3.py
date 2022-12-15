# Создать декоратор simple_decorator с "хорошим поведением", то есть 

# декоратор при котором происходит сохранение "магических" полей __name__  и  __doc__

# Должны проходиться тесты

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result.__name__ = args[0].__name__
        result.__doc__ = args[0].__doc__
        return result
    return wrapper


@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        return func(*args, **kwargs)
    return you_will_never_see_this_name


@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x


assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'

print(double(155))