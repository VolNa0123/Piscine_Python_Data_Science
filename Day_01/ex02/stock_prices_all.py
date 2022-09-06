import sys

def stock_prices(company):
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
    if company not in COMPANIES:
        return 'Unknown company'
    return STOCKS[COMPANIES[company]] # companies[company] - значение из первого списка, которое становится ключом ко второму


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(stock_prices(sys.argv[1].capitalize())) # .capitalize() в строке делает первую букву заглавной, остальные строчными