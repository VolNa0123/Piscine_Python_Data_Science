def dict_sorter():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    # Создадим из списка словарь (нужно по заданию)
    my_dict = dict((x, y) for x, y in list_of_tuples)
    print(1)
    print(my_dict)

    # Отсортируем страны по алфавиту так как удобно сортировать по ключу
    # Сортировка возвращает список
    sorted_list = sorted(my_dict.items(), key=lambda item: item[0])
    print(2)
    print(sorted_list)

    # Для второй сортировки опять создадим словарь
    sorted_dict = {k: v for k, v in sorted_list}
    print(3)
    print(sorted_dict)

    # Теперь отсортируем по убыванию номера '-' перед полем сортировки позволяет сортировать по убыванию
    sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))
    print(4)

    # Опять все соберем в словарь.
    # Это можно не делать, список уже правильно отсортирован, можно просто выводить нужные поля
    sorted_dict = {k: v for k, v in sorted_list}
    print(sorted_dict)
    print(5)
    
    # Выведем в том виде, как просят в задании
    for i in sorted_dict :
        print('%s' % i)
    
if __name__ == '__main__':
    dict_sorter()

# https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/sortirovka-slovarja-znacheniju-kljuchu/
# https://pythonru.com/osnovy/vozmozhnosti-i-primery-funkcii-sorted-v-python