def data_types():

    a = 1
    b = 'Hello'
    c = 1.2
    d = True
    e = ['1', '2'] # список упорядоченный, изменяемый
    f = {'name': 'mcherrie', 'location': 'at-g5'} # словарь упорядоченный, изменяемый
    g = ('Hello', 1, True) # кортеж упорядоченный, НЕизменяемый
    h = set() # множество НЕупорядоченный, изменяемый

    print('[%s, %s, %s, %s, %s, %s, %s, %s]'
          % (
              type(a).__name__, type(b).__name__ , #__name__ для того, чтобы выводилось только имя класса
              type(c).__name__, type(d).__name__,
              type(e).__name__, type(f).__name__ ,
              type(g).__name__, type(h).__name__
            )
          )
          
if __name__ == '__main__':
    data_types()

# Полезные ссылки:
# https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/lists.html
# https://foxford.ru/wiki/informatika/mnozhestva-v-python