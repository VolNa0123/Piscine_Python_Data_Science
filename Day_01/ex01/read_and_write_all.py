def read_and_write():
    infile = open('hh.csv', 'r')
#    text = infile.read().replace('\",\"', '\"\t')
    outfile = open('hh.tsv', 'w')
 #   outfile.write(text)
    outfile.write(infile.read().replace('\",\"', '\"\t'))

if __name__ == '__main__':
    read_and_write()

# Надо добавить в папку файл hh.csv из ex01 Day00
# https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html