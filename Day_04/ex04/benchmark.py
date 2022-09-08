import timeit
from random import randint
from collections import Counter

lst = [randint(0, 100) for i in range(100000)]

def my_function(lst):
    dict_all = {}
    for element in lst:
        if element not in dict_all:
            dict_all[element] = 1
        else:
            dict_all[element] += 1
    return dict_all

def my_top(lst):
    # Создадим словарь из списка
    my_dict = my_function(lst)
    # Отсортируем, получим список
    sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))
    # Возьмем срез первых десяти
    top_list = sorted_list[:10]
    # Создадим из списка словарь (нужно по заданию)
    my_top_dict = dict((x, y) for x, y in top_list)
    return my_top_dict

def counter_dict(list):
    return dict(Counter(list))

def counter_top_10(list):
    return Counter(list).most_common(10)

def benchmark():
    lst = [randint(0, 100) for i in range(100000)]
    print('my function:', timeit.timeit(f'my_function({lst})',
                        number=1,
                        setup='from __main__ import my_function'))

    print('Counter:', timeit.timeit(f'counter_dict({lst})',
                        number=1,
                        setup='from __main__ import counter_dict'))

    print('my top:', timeit.timeit(f'my_top({lst})',
                    number=1,
                    setup='from __main__ import my_top'))

    print("Counter's top:", timeit.timeit(f'counter_top_10({lst})',
                        number=1,
                        setup='from __main__ import counter_top_10'))
    
if __name__ == '__main__':
    benchmark()

# Counter: https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/