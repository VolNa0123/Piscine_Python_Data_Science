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

    # Отсортируем страны по алфавиту так как удобно сортировать по ключу
    # Сортировка возвращает список
    sorted_list = sorted(my_dict.items(), key=lambda item: item[0])

    # Для второй сортировки опять создадим словарь
    sorted_dict = {k: v for k, v in sorted_list}

    # Теперь отсортируем по убыванию номера '-' перед полем сортировки позволяет сортировать по убыванию
    sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))

    # Опять все соберем в словарь.
    sorted_dict = {k: v for k, v in sorted_list}
    
    for i in sorted_dict :
        print('%s' % i)
    
if __name__ == '__main__':
    dict_sorter()

# https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/sortirovka-slovarja-znacheniju-kljuchu/
# https://pythonru.com/osnovy/vozmozhnosti-i-primery-funkcii-sorted-v-python