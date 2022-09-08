import timeit
import sys
from functools import reduce

# Функция находит сумму квадратов до заданного числа с помощью цикла
def loop_and_sum(n):
    sum_square = 0
    for i in range(1, n + 1):
        sum_square += i * i
        return sum_square

# Функция находит сумму квадратов до заданного числа с помощью reduce
def reduce_and_sum(n):
    sum_square = reduce(lambda y, x: y + x**2, range(1, n+1))
    return sum_square

def benchmark(command, n_of_calls, n_for_sum):
    SETUP_CODE = f'from __main__ import {command}'
    TEST_CODE = f'{command}({n_for_sum})'
    times = timeit.timeit(setup = SETUP_CODE, stmt = TEST_CODE, number = n_of_calls)
    print(times)

if __name__ == '__main__':
    if sys.argv[1] == 'loop':
        command = 'loop_and_sum'
    else:
        command = 'reduce_and_sum'
    benchmark(command, int(sys.argv[2]), int(sys.argv[3]))

# http://pythonicway.com/python-functinal-programming