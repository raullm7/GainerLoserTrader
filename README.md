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

To run it you can just run the script I made: `./cron_starter.sh`
IMPORTANT: You will have to modify the absolute paths in this file as well as they PATH variable.
To know your path variable simply go to the directory where you run the script and run `echo $PATH`

If you are new with `Crontab` here there is a good cheat sheet: `https://www.codementor.io/akul08/the-ultimate-crontab-cheatsheet-5op0f7o4r`

ENJOY!


# Troubleshooting

`ValueError: unsupported pickle protocol: 3` This basically means that you are running Python 2 instead of Python 3.
They pickle library will fail to load the data since the protocols changed from Python 3 to Python 2.
Just run it with Python 3 and you should not see it again ;).