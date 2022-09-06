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

def all_stocks():
    if len(sys.argv) != 2:
        return

    COMPANIES, STOCKS = data()
    words = sys.argv[1].replace(' ', '').split(',')
    for word in words:
        if not word:
            print('')
            return # если нет слов, перевод на новую строку
    for word in words:
        if word.upper() in STOCKS:
            print("%s is a ticker symbol for %s"
                % (word.upper(), get_key(COMPANIES, word.upper())))
        elif word.capitalize() in COMPANIES:
            print("%s stock price is %s"
                % (word.capitalize(), STOCKS[COMPANIES[word.capitalize()]]))
        else:
            print("%s is an unknown company or an unknown ticker symbol"
                % (word))

if __name__ == '__main__':
    all_stocks()