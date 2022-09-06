import sys

def names_extractor():
# Контекстный менеджер with сам закроет файл после прочтения и позаботится об ошибках
  with open('employees.tsv', 'a') as f_write: # 'a' чтобы write дозаписывал, а не перезаписывал
    f_write.write('Name\tSurname\tE-mail\n')
# Файл email.tsv(любой ваш) должен лежать в этой же директории
    with open('email.tsv', 'r') as f_read:
      line = f_read.readlines() # создали список строк файла(отдельных email)
      for i in range(len(line)):
        name = line[i].split('@')[0].split('.')[0]
        surname = line[i].split('@')[0].split('.')[1]
        f_write.write(f'{name.capitalize()}\t{surname.capitalize()}\t{line[i]}')

if __name__ == '__main__':
  if len(sys.argv) != 2:
    raise Exception("Error argument")
  names_extractor()

# При запуске аргумент - файл email.tsv
# Про контекстный менеджер with:
# https://pythononline.ru/osnovy/operator-with-python-menedzhery-konteksta
# Чтение из файла и запись в файл:
# https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod