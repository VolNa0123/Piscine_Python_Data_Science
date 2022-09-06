import sys

def data():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return COMPANIES, STOCKS

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

def find_element(elem):
    COMPANIES, STOCKS = data()
    elem_cap = elem.capitalize()
    elem_up = elem.upper()
    if elem_cap in COMPANIES:
        return f'{elem_cap} stock price is {STOCKS[COMPANIES[elem_cap]]}' #f-строки форматируют строку, подставляя нужные значения
    elif elem_up in STOCKS:
        return f'{elem_up} is a ticker symbol for {get_key(COMPANIES, elem_up)}'
    return f'{elem} is an unknown company or an unknown ticker symbol'

def all_stocks():
    if len(sys.argv) != 2:
        return

    string_split = sys.argv[1].replace(',', ' , ').split()
    commas_num = string_split.count(',')
    if commas_num * 2 + 1 == len(string_split):
        for elem in string_split:
            if elem != ',':
                print(find_element(elem.strip(',')))

if __name__ == '__main__':
    all_stocks()