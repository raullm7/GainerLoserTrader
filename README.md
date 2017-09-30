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
      
      `data = {'sold':True, 'wallet':{}, 'money':0}`
      
      `with open('data.txt', 'wb') as f:
          pickle.dump(data, f)`
  3. Run the program whenever you want!
  
I run it at specefic hours from a Mac, for that scheduling of scripts I use crontab.
