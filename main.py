import requests
import pickle
from bs4 import BeautifulSoup
from bs4 import Tag


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


def sell_outside(name, value, money):
    sell_url = 'https://min-api.cryptocompare.com/data/price?fsym=' + str(name) + '&tsyms=USD'
    sell_response = requests.get(sell_url)
    data = sell_response.json()
    try:
        money += int(data['USD'])
    except ValueError:
        money -= value
    return money


def buy(info, money, wallet):
    prices = info['prices']
    names = info['names']

    for index in range(0, len(prices) - 1):
        if is_in_wallet(names[index], wallet):
            wallet[str(names[index])] = float(wallet.get(str(names[index]))) + float(prices[index])
        else:
            wallet[str(names[index])] = float(prices[index])
        money -= float(prices[index])

    return {'wallet':wallet, 'money':money}


def sell(info, money, wallet):
    prices = info['prices']
    names = info['names']

    for name, value in wallet:
        if name in names:
            money += prices[names.index(name)]
        else:
            money = sell_outside(name, value, money)

        wallet[name] = 0

        return {'wallet': wallet, 'money': money}


with open('data.txt', 'rb') as f:
    data = pickle.load(f)

# sold is True if last movement was to sell, 0 otherwise
sold = data['sold']
total_money = data['money']
my_wallet = data['wallet']

data['sold'] = not data['sold']

url = 'https://coinmarketcap.com/gainers-losers/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

div_hour = soup.find("div", { "id" : "gainers-1h" })
info_hour = get_info(div_hour)

div_day = soup.find("div", { "id" : "gainers-24h" })
info_day = get_info(div_day)

div_week = soup.find("div", { "id" : "gainers-7d" })
info_week = get_info(div_week)

if sold:
    data = buy(info_day, total_money, my_wallet)
else:
    data = sell(info_day, total_money, my_wallet)

with open('data.txt', 'wb') as f:
    pickle.dump(data, f)