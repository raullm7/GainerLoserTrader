import pickle
import time
import requests


def get_json(url):
    counter = 0
    try:
        sell_response = requests.get(url)
        data = sell_response.json()
        return data
    except:
        # If I have tried to connect less than 10 times
        if counter < 10:
            print(url + ' is not responding.')
            print('Sleeping 60s and trying again...')
            time.sleep(60)
            get_json(url)
        else:
            print('TIMEOUT ERROR!')
            exit()

def money_in_wallet(wallet):
    total_money = 0
    for key, value in wallet.items():
        sell_url = 'https://min-api.cryptocompare.com/data/price?fsym='\
                   + str(key) + '&tsyms=USD'

        data = get_json(sell_url)
        try:
            total_money += float(data['USD'])
        except (ValueError, KeyError):
            total_money += value
    return total_money


def print_data(file, wallet, money):
    if not wallet:
        return

    wallet_money = money_in_wallet(wallet)

    percentage = money / 1000.0 * 100

    print('\nFILE NAME: ' + file)

    print('Time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

    print('Actual amount of money: ' + str(money))
    print('Compared with initial investment (1000): ' + str(percentage) + '%')

    print('Total money if I sold everything now: ' + str(wallet_money + money))

    print('Wallet: \n' + str(wallet))


files = ['data.txt', 'data_1h.txt', 'data_24h.txt']

for file in files:
    with open(file, 'rb') as f:
        data = pickle.load(f)

    wallet = data['wallet']
    money = data['money']
    print_data(file, wallet, money)



