import math
import datetime


def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, math.ceil(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def primes(max_value=math.inf):
    i = 1
    while True:
        if i > max_value:
            break
        if isprime(i):
            yield i
        i += 1


def gendates(month, day, year):
    date = datetime.datetime(year, month, day)
    while True:
        yield date
        date += datetime.timedelta(days=1)


def gendow(month, day, year):
    days = ["Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье"]
    day = datetime.datetime(year, month, day).weekday()
    while True:
        yield days[day]
        day = (day+1) % 7


def gen_all_day_info(month, day, year):
    day_name = gendow(month, day, year)
    for d in gendates(month, day, year):
        yield d.day, d.month, d.year, day_name.__next__()


def head(*filenames, count=10):
    for filename in filenames:
        output = f"==> {filename} <=="
        with open(filename, 'r', encoding="utf8") as f:
            lines = f.readlines()
        for line_no, line in enumerate(lines, 0):
            if line_no < count:
                output += "\n" + line
        yield output


def main():

    print("Prime numbers:")
    for i in primes(100):
        print(i, end=" ")
    print()

    print("Dates from 1.01.2022:")
    for i in gendates(1,1,2022):
        print(i)
        if i > datetime.datetime(2022, 3, 1):
            break
    print()

    print("WeekDays from 1.01.2022:")
    count = 0
    for i in gendow(1,1,2022):
        print(i)
        if count > 10:
            break
        count += 1
    print()

    print("All day info from 1.01.2022:")
    count = 0
    for i in gen_all_day_info(1, 1, 2022):
        print(i)
        if count > 10:
            break
        count += 1
    print()

    print("First lines in files:")
    for data in head("file.txt", "littleFile.txt", 5):
        print(data)
        print()


if __name__ == '__main__':
    main()
