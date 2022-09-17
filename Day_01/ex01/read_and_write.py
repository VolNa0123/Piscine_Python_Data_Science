def read_and_write(filename):
    file_csv = open(filename+'.csv', 'r')
    file_tsv = open(filename+'.tsv', 'w')
    file_tsv.write(file_csv.read()
            .replace('\",\"', '\"\t\"')
            .replace(',false', '\tfalse\t')
            .replace(',\"', '\"')
            .replace(',true', '\ttrue\t'))
    file_csv.close()
    file_tsv.close()

if __name__ == '__main__':
    read_and_write('ds')

# Надо добавить в папку файл hh.csv из ex01 Day00
# https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html