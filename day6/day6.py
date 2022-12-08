
#%%
from typing import List, Dict
from collections import Counter

# %%
def findMarker(signal):
    for index in range(4,len(signal)):
        subSignal = signal[index-4:index]
        if len(set(subSignal)) == 4:
            print(
                len(subSignal) + index-4
            )
            break
def findMessage(signal):
    messageLen = 14
    for index in range(4,len(signal)):
        subSignal = signal[index-messageLen:index]
        if len(set(subSignal)) == messageLen:
            print(
                len(subSignal) + index-messageLen
            )
            break

signals = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg'
]
for signal in signals:
    findMarker(signal)

# %%
with open('input.txt','r') as f:
    actualSignal = f.read()

findMarker(actualSignal)
# %%
for signal in signals:
    findMessage(signal)

# %%
findMessage(actualSignal)
# %%
