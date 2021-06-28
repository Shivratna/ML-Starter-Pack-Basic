import numpy as np
import json

with open('test2.txt', 'r') as file:
    data = file.read().replace('\n', '')

seed = input("Enter seed: ")
def genTable(data , k = 5):
    Table = {}

    for i in range(len(data) - k):
        X = data[i:i+k]
        Y = data[i+k]

        if Table.get(X) is None:
            Table[X] = {}
            Table[X][Y] = 1
        else:
            if Table[X].get(Y) is None:
                Table[X][Y] = 1
            else:
                Table[X][Y] += 1
    return Table

Table = genTable( data.lower() )

def predic(seed , k=5):
    inp = seed[ -k : ]
    poss = Table[inp]

    freq = list(poss.values())
    
    options = list(poss.keys())

    probabs = [ele/sum(freq) for ele in freq]

    nextchar = np.random.choice( options , p = probabs)
    return nextchar

for i in range(1000):
    nextchar = predic(seed)
    seed = seed + nextchar

store = open("mind.txt",'w+')
store.write(json.dumps(Table))

print(seed)

