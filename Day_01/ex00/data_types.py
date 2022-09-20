def data_types():

    a = 0
    b = 'str'
    c = 0.0
    d = True
    e = ['1', '2']
    f = {}
    g = ('a', 2, True)
    h = set(g)

    vars =  [
            type(a).__name__, type(b).__name__ ,
            type(c).__name__, type(d).__name__,
            type(e).__name__, type(f).__name__ ,
            type(g).__name__, type(h).__name__
            ]

    print(vars)
          
if __name__ == '__main__':
    data_types()
