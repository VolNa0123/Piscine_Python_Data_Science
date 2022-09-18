from config import *
from analytics import Research
import logging
import json
import requests

    # Отправим сообщение в телеграмм
def send_in_telegramm(text):
    token = "5464113755:AAFN0dPEiUnsamwtzTa6HkhUJWSjWwo21V8"
    chat_id = "498146952"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
    results = requests.get(url_req)
    if results.status_code != 200:
        raise Exception(f'Error server {results.status_code}')

def check_arg(file_name):
    logging.info("Check arguments")
    with open(file_name, 'r') as file:
        line = file.readlines()
        # Если пустой файл или одна строка, но не с нужными значениями, то исключение
        if len(line) == 0 or (len(line) == 1 and (line[0] != '0,1\n' and line[0] != '1,0\n')):
            send_in_telegramm('The report hasn’t been created due to an error')
            raise Exception("Error argument")
        # Проверяем остальные строки на нужные значения
        if len(line) > 1:
            for i in range(1, len(line) - 1):
                if line[i] != '0,1\n' and line[i] != '1,0\n':
                    send_in_telegramm('The report hasn’t been created due to an error')
                    raise Exception("Error argument")

# У меня на машине для правильного запуска надо запустить виртуальную машину,
# так как конфликт версий питона и не импортируется requests
# надо написать в командной строке 
# mkdir test          
# python3 -m venv test
# source test/bin/activate
# pip3 install requests
# после этого запускать
def main():
    logging.basicConfig(filename=f'{LOG_FILE}.{EXTENSION_LOG}', 
                        format='%(asctime)s %(message)s',
                        datefmt='%y-%d-%m %H:%M:%S',
                        filemode='w',
                        level=logging.DEBUG)
    if check_arg(FILEPATH):
        send_in_telegramm('The report hasn’t been created due to an error')
        raise Exception("Error argument")
    output = Research(FILEPATH).file_reader()
    element = Research.Calculations(output)
    predict = Research.Analytics(3)
    observations = len(output)
    heads_count = element.count[0]
    tails_count = element.count[1]
    heads_fractions = round(element.fractions[0], 2)
    tails_fractions = round(element.fractions[1], 2)
    predict_heads_count = predict.count[0]
    predict_tails_count = predict.count[1]

    report = REPORT.format(
        observations, 
        tails_count,
        heads_count, 
        tails_fractions,
        heads_fractions,
        NUM_OF_STEPS,
        predict_heads_count,
        predict_tails_count
        )

    Research.Analytics.save_file(report, REPORT_FILE, EXTENSION)
    send_in_telegramm('The report has been successfully created')
    

if __name__ == '__main__':
    main()

# logging: https://overcoder.net/q/53568/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82-%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D0%B2-python
# logging: https://docs-python.ru/standart-library/paket-logging-python/funktsija-basicconfig-modulja-logging/
# requests: https://python.ru/post/97/