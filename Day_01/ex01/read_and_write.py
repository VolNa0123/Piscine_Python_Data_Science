def read_and_write(filename):
    file_csv = open(filename+'.csv', 'r')
    file_tsv = open(filename+'.tsv', 'w')
    file_tsv.write(file_csv.read().replace('\",\"', '\"\t'))

if __name__ == '__main__':
    read_and_write('hh')

# Надо добавить в папку файл hh.csv из ex01 Day00