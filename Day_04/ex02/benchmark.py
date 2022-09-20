import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
emails = emails * 5

# Функция выбирает элементы из списка по условию и добавляет их в новый с помощью цикла
def loop():
    new_emails = []
    for element in emails:
        if (element.find('@gmail.com') > 0): # Если элемент содержит @gmail.com, то добавляем его
            new_emails.append(element)
    return new_emails

# Функция выбирает элементы из списка по условию и добавляет их в новый в определении списка
def list_comprehension():
    new_emails = [element for element in emails if element.find('@gmail.com') > 0]
    return new_emails

# Функция выбирает элементы из списка по условию и добавляет их в новый методом map
def with_a_map():
    new_emails = map(lambda x: x if (element.find('@gmail.com')) else None , emails)
    return new_emails

# Функция выбирает элементы из списка по условию и добавляет их в новый методом filter
def with_a_filter():
    new_emails = filter(lambda x: x if (element.find('@gmail.com')) else None , emails)
    return new_emails

def benchmark(function, n_of_calls):
    SETUP_CODE = f'from __main__ import {function}'
    times = timeit.timeit(setup = SETUP_CODE, number = n_of_calls)
    print(times)

if __name__ == '__main__':
    benchmark(sys.argv[1], int(sys.argv[2]))