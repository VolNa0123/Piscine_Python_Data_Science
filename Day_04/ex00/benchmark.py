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

# https://dvmn.org/encyclopedia/qna/5/chto-takoe-list-comprehension-zachem-ono-kakie-esche-byvajut/
# Функция выбирает элементы из списка по условию и генерирует из них список
def list_comprehension():
    new_emails = [element for element in emails if element.find('@gmail.com') > 0]
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

if __name__ == '__main__':
    time_1 = time_loop()
    time_2 = time_comprehension()
    if (time_2 < time_1):
        print('it is better to use a list comprehension')
        print(time_2, 'vs', time_1)
    else:
        print('it is better to use a loop')
        print(time_1, 'vs', time_2)
