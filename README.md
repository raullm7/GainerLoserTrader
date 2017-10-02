# GainerLoserTrader
Experiment to check how a simple algorithm performs investing in gainer/losers cryptocurrencies.
APIs used:
  - Cryptocompare: Used to get the price of a given cryptocurrency at any moment.
  - Coinmarketcap: I have used their website to parse the gainer/losers cryptocurrencies
      https://coinmarketcap.com/gainers-losers

To run the project you will need to create a new 'data.txt' with an empty dictionary created with pickle:

  1. Open a python 3 terminal.
  2. Type into the terminal:
  
      `import pickle`
      
      `data = {'wallet':{}, 'money':1000}`
      
      `with open('data.txt', 'wb') as f:
          pickle.dump(data, f)`
  3. Run the program whenever you want!

  OR you can just run `python start.py` ...

To check your 'wallet' balance just run `python check.py`
  
I run it at specefic hours from a Mac, for that scheduling of scripts I use crontab.

To run it you can just install crontab: `pip3 install python-crontab` and then `python run.py`
Its very easy to modify, leave a good beginners manual here: `https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231`


# Troubleshooting

`ValueError: unsupported pickle protocol: 3` This basically means that you are running Python 2 instead of Python 3.
They pickle library will fail to load the data since the protocols changed from Python 3 to Python 2.
Just run it with Python 3 and you should not see it again ;).