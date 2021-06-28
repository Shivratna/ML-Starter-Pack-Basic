#import requests
import numpy as np
import json

learnt = open('D:\INIT2021\Basic-ML-Training-master\mind.txt', 'r')
Table = json.loads(learnt.read())
seed = input("Enter seed: ")

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

print(seed)

