#%%
directory = '/home/sp/Insync/c3126951@uon.edu.au/OneDrive/coding\ projects/'
with open('input.txt', 'r') as f:
    text = f.read()

max([sum([int(number) for number in numbersList.split('\n') if number != '']) for numbersList in text.split('\n'*2)])

# %%
resultForAllLists = []
for numberList in text.split('\n'*2):
    resultForList = []
    for number in numberList.split('\n'):
        if number != '':
            resultForList.append(int(number))
    resultForAllLists.append(sum(resultForList))
max(resultForAllLists)

# %%
# %%
import pandas as pd
# %%
processed = [(count, value) for count, value in enumerate([
    sum([
        int(number) for number in numbersList.split('\n') if number != ''
    ]) for numbersList in text.split('\n'*2)
])]
# %%
import pandas as pd

with open('input.txt', 'r') as f:
    text = f.read()

sum(
    pd.DataFrame(
        columns=['elfIndex','calories'],
        data = [(count, value) for count, value in enumerate([
            sum([int(number) for number in numbersList.split('\n') if number != '']) for numbersList in text.split('\n'*2)
    ])]).sort_values('calories', ascending=False).calories.values[:3]
)

# %%
df = pd.DataFrame(
    columns=['elfIndex','calories'],
    data = processed)

sum(df.sort_values('calories', ascending=False).calories.values[:3])
# %%
