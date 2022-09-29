import numpy
import matplotlib


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def number_addition():
    current_value = 0
    last_value = -1
    while current_value != last_value:
        last_value = current_value
        current_value += int(input('Введите число: '))
    return current_value


def vis_main():
    year = int(input('Введите год: '))
    if is_leap_year(year):
        print('Високосный год')
    else:
        print('Не високосный год')


def num_main():
    print(f'Итоговая сумма: {number_addition()}')


if __name__ == '__main__':
    num_main()
