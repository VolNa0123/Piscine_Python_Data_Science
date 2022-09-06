import sys

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_reader(self, has_header = True):
        with open(self.file_name, 'r') as file:
            line = file.readlines()
            if line[0] == '0,1\n' or line[0] == '1,0\n':
                self.has_header = False
            # Если заголовок есть, то начнем записывать со второй строки (start = 1), иначе - с первой
            start = 0
            if has_header == True:
                start = 1
            list_lists = []
            for i in range(start, len(line)):
                list_i = [int(line[i][0])]
                list_i.append(int(line[i][2]))
                list_lists.append(list_i)
            return(list_lists)

    class Calculations:
        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fractions = self.fractions()

        def counts(self):
            x = [x[0] for x in self.data]
            y = [y[1] for y in self.data]
            return [sum(x), sum(y)]

        def fractions(list_counts):
            return [(counts[0] / (counts[0] + counts[1])) * 100,
                    (counts[1] / (counts[0] + counts[1])) * 100]


def check_arg(file_name):
    with open(file_name, 'r') as file:
        line = file.readlines()
        # Если пустой файл или одна строка, но не с нужными значениями, то исключение
        if len(line) == 0 or (len(line) == 1 and (line[0] != '0,1\n' and line[0] != '1,0\n')):
            raise Exception("Error argument")
        # Проверяем остальные строки на нужные значения
        if len(line) > 1:
            for i in range(1, len(line) - 1):
                if line[i] != '0,1\n' and line[i] != '1,0\n':
                    raise Exception("Error argument")

if __name__ == '__main__':
    if len (sys.argv) != 2 or check_arg(sys.argv[1]):
        raise Exception("Error argument")
    list_lists = Research(sys.argv[1]).file_reader()
    print(list_lists)
    list_counts = Research.Calculations.counts(list_lists)
 #   print(list_counts[0], list_counts[1])
 #   list_fractions = Research.Calculations.fractions(list_counts)
#    print(list_fractions[0], list_fractions[1])

# https://younglinux.info/oopython/init