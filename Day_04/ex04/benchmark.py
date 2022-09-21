import timeit
from random import randint
from collections import Counter

def lst_to_dict(lst):
	dict_all = {}
	for element in lst:
		if element not in dict_all:
			dict_all[element] = 1
		else:
			dict_all[element] += 1
	return dict_all

def my_top_dict(lst):
	# Создадим словарь из списка
	my_dict = lst_to_dict(lst)
	# Отсортируем, получим список
	sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))
	# Возьмем срез первых десяти
	top_list = sorted_list[:10]
	# Создадим из списка словарь (нужно по заданию)
	my_top_dict = dict((x, y) for x, y in top_list)
	return my_top_dict

def counter_dict(lst):
	return dict(Counter(lst))

def counter_top_10(lst):
	return Counter(lst).most_common(10)

def my_time(func_name, lst):
	times = timeit.timeit(lambda: func_name(lst), number = 1)
	return times
	
if __name__ == '__main__':
	
	lst = [randint(0, 100) for i in range(1000000)]
	try:
		print('my function:', my_time(lst_to_dict, lst))
		print('Counter:', my_time(counter_dict, lst))
		print('my top:', my_time(my_top_dict, lst))
		print('Counter\'s top:', my_time(counter_top_10, lst))
	except:
		print('ERROR')




#list comprehensions - генератор списков
#map - идет по списку, применяет какую-то функцию к каждому элементу
#filter - то же самое что и map, только по-другому
#reduce - Применяет указанную функцию к элементам последовательности. на выходе одно значение
#counter - Встроенный модуль из библиотеки для подсчетов