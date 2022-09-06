import sys

def caesar(code, phrase, n):
    if code == 'decode':
        n *= -1
    new_phrase = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Пройдемся по каждой букве фразы
    for i in range(len(phrase)):
    # Если это буква, заменим ее в соответствии со сдвигом
        if phrase[i] in alphabet:
            m = alphabet.find(phrase[i])
    # Сдвиг зациклим через остатки от деления
            new_phrase += alphabet[(n + m) % len(alphabet)]
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