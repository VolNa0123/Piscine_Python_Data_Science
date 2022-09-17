import sys

def caesar(code, phrase, n):
    if code == 'decode':
        n *= -1
    new_phrase = ''
    alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Пройдемся по каждой букве фразы
    # Если это буква, заменим ее в соответствии со сдвигом
    # Сдвиг зациклим через остатки от деления
    for i in range(len(phrase)):
        if phrase[i] in alphabet1:
            m = alphabet1.find(phrase[i])
            new_phrase += alphabet1[(n + m) % len(alphabet1)]
        elif phrase[i] in alphabet2:
            m = alphabet2.find(phrase[i])
            new_phrase += alphabet2[(n + m) % len(alphabet2)]
    # Если это не буква, просто скопируем
        else:
            new_phrase += phrase[i]

    print(new_phrase)

if __name__ == '__main__':
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        raise Exception("Error argument")
    if not sys.argv[2].isascii():
        raise Exception("Error: str not from ascii")
    try:
        n_shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Error: shift is not int")
    caesar(sys.argv[1], sys.argv[2], n_shift)