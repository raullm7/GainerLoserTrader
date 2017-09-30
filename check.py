import pickle

with open('data.txt', 'rb') as f:
    data = pickle.load(f)

print(data)