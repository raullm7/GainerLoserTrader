import pickle

data = {'sold':True, 'wallet':{}, 'money':100}

with open('data.txt', 'wb') as f:
    pickle.dump(data, f)