import sys

def letter_starter():
  with open('employees.tsv', 'r') as f_read:
    line = f_read.readlines() # Cоздадим список строк файла(отдельных email)
    name = '' # Вводим для случая, если подали неизвестный или некорректный email
    for i in range(len(line)):
      if line[i].split('\t')[2] == sys.argv[1] + '\n': # Если email совпал с заданным, выполняем
        name = line[i].split('\t')[0]
        print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
    if name == '': # Если заданный email не встретился выводим ошибку
      print('Error email')

if __name__ == '__main__':
    if len (sys.argv) != 2:
        raise Exception("Error argument")
    letter_starter()

# При запуске аргумент - конкретный адрес из email.tsv, names_extractor уже отработал