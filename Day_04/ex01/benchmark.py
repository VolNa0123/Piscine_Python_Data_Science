import timeit

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
emails = emails * 5

# Функция выбирает элементы из списка по условию и добавляет их в новый с помощью цикла
def loop_and_an_append():
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

# Считаем время выполнения первой функции 90 000 000 раз
def time_loop():
    SETUP_CODE = 'from __main__ import loop_and_an_append'
    times = timeit.timeit(setup = SETUP_CODE, number = 9 * 10 ** 7)
    return times     

# Считаем время выполнения второй функции 90 000 000 раз
def time_comprehension():
    SETUP_CODE = 'from __main__ import list_comprehension'
    times = timeit.timeit(setup = SETUP_CODE, number = 9 * 10 ** 7)
    return times

# Считаем время выполнения третьей функции 90 000 000 раз
def time_map():
    SETUP_CODE = 'from __main__ import with_a_map'
    times = timeit.timeit(setup = SETUP_CODE, number = 9 * 10 ** 7)
    return times

if __name__ == '__main__':
    time_1 = time_loop()
    time_2 = time_comprehension()
    time_3 = time_map()
    # Для удобства сравнения времен создадим кортеж, т.к. его удобно сортировать
    times = (time_1, time_2, time_3)
    times = tuple(sorted(times))
    if (times[0] == time_1):
        print('it is better to use a loop')
    elif (times[0] == time_2):
        print('it is better to use a list comprehension')
    elif (times[0] == time_3):
        print('it is better to use a map')
    print(f'{times[0]} vs {times[1]} vs {times[2]}')
