import pickle

data = {'wallet':{}, 'money':1000, 'money_after_movement': -1000}

files = ['data.txt', 'data_1h.txt', 'data_24h.txt']

for file in files:
    with open(file, 'wb') as f:
        pickle.dump(data, f)