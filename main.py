#!/usr/bin/env python3

import requests
import pickle
from bs4 import BeautifulSoup
from bs4 import Tag
import sys
from time import sleep


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
            sleep(60)
            get_json(url)
        else:
            print('TIMEOUT ERROR!')
            exit()


def get_info(div):
    for tr in div:
        if isinstance(tr, Tag):
            names = []
            currency_names_td = tr.find_all('td', {'class': 'text-left'})
            for currency_name in currency_names_td:
                names.append(currency_name.string)

            prices = []
            currency_prices = tr.find_all('a', {'class': 'price'})
            for price in currency_prices:
                if isinstance(price, Tag):
                    prices.append(price['data-usd'])

    return {'names':names, 'prices':prices}


def is_in_wallet(currency, wallet):
    return not isinstance(wallet.get(str(currency)), type(None))


def buy(info, money, wallet):
    prices = info['prices']
    names = info['names']

    for index in range(0, len(prices) - 1):
        if is_in_wallet(names[index], wallet):
            wallet[str(names[index])] = float(wallet.get(str(names[index])))\
                                        + float(prices[index])
        else:
            wallet[str(names[index])] = float(prices[index])
        money -= float(prices[index])

    return {'wallet':wallet, 'money':money}


def sell(money, wallet):
    for key, value in wallet.items():
        sell_url = 'https://min-api.cryptocompare.com/data/price?fsym=' \
                   + str(key) + '&tsyms=USD'
        data = get_json(sell_url)
        try:
            money += float(data['USD'])
        except (ValueError, KeyError):
            money += value

        del wallet[str(key)]
    return {'wallet': wallet, 'money': money}

# Main takes arg 'every_h' which is true (1) if main is executed
# at a multiple of the original hour (controlled by run.py),
# false (0) otherwise
# By default every_h takes value 1 (True)
try:
    every_h = float(sys.argv[1])
except (ValueError, IndexError) as e:
    if type(e) is ValueError:
        print('ERROR: ' + str(e))
    every_h = 1

if every_h:
    file = 'data_1h.txt'
else:
    file = 'data_24h.txt'

with open(file, 'rb') as f:
    data = pickle.load(f)

total_money = data['money']
my_wallet = data['wallet']

original_money = data['money']

url = 'https://coinmarketcap.com/gainers-losers/'

# If the computer has no internet connection or API fails, exit
try:
    response = requests.get(url)
except:
    print('ERROR: No internet connection')
    exit()

html = response.content

soup = BeautifulSoup(html, 'html.parser')

if every_h:
    div = soup.find("div", { "id" : "gainers-1h" })
else:
    div = soup.find("div", { "id" : "gainers-24h" })
# Weekly not needed yet
# div = soup.find("div", { "id" : "gainers-7d" })

info = get_info(div)

# The first time I only buy
if not my_wallet:
    data = buy(info, total_money, my_wallet)
else:
    # Then I sell and buy again with updated cryptocurrencies
    data = sell(total_money, my_wallet)
    data = buy(info, total_money, my_wallet)

with open(file, 'wb') as f:
    pickle.dump(data, f)