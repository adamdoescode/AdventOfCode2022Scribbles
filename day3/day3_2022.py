# %%
from typing import List
from string import ascii_uppercase, ascii_lowercase
# %%

class RucksackReorder():
    def __init__(self) -> None:
        self.itemPriorityLower = dict(zip(ascii_lowercase,range(1,27)))
        self.itemPriorityUpper = dict(zip(ascii_uppercase,range(27,27+26)))

    def reorder(self, AllRucksacks: str) -> int:
        sumOfPriorities = 0
        for rucksack in AllRucksacks.strip().split('\n'):
            #assumes rucksacks have len(rucksack)%2 == 0
            #add this error handling incase not the case and then we can sort it out
            if len(rucksack) % 2 != 0:
                raise ValueError("Rucksack length must be even")
            #since order is unimportant we can sort the compartments for speed
            firstCompartment = ''.join(sorted(rucksack[int(len(rucksack)/2):]))
            secondCompartment = ''.join(sorted(rucksack[:int(len(rucksack)/2)]))
            #process the compartments so that:
            #initialise
            for item in firstCompartment:
                if item in secondCompartment:
                    PriorityTemp = 0
                    if item.islower():
                        PriorityTemp += self.itemPriorityLower[item]
                    else:
                        PriorityTemp = self.itemPriorityUpper[item]
                    sumOfPriorities += PriorityTemp
                    print(
                        item, PriorityTemp
                    )
                    break
        return sumOfPriorities

exampleInput = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

RucksackReorder().reorder(exampleInput)

# %%
with open('input.txt') as f:
    realInput = f.read()

RucksackReorder().reorder(realInput)

# %%
class BadgePriorities(RucksackReorder):
    '''
    We want this class to inherit the item priority dictionaries from the 
    RucksackReorder class
    '''

    def calculateSingleGroupPriority(self, RucksackGroup: List[str]) -> int:
        '''Find the common item and return the sum of their priorities'''
        GroupPriority = 0
        #we will always have a list of 3 rucksacks
        rucksacks = RucksackGroup
        for itemR1 in rucksacks[0]:
            for itemR2 in rucksacks[1]:
                for itemR3 in rucksacks[2]:
                    if itemR1 == itemR2 == itemR3:
                        if itemR1.islower():
                            GroupPriority += self.itemPriorityLower[itemR1]
                        else:
                            GroupPriority = self.itemPriorityUpper[itemR1]
                        print(
                            itemR1, itemR2, itemR3, GroupPriority
                        )
                        return GroupPriority

    def proccessAllGroups(self, AllElves: str) -> int:
        sumOfPriorities = 0
        #pass each group (3 lines each) to the group Priority class
        RucksackGroup = []
        ElfGroups = [rucksack for rucksack in AllElves.strip().split('\n')]
        for index in range(1,len(ElfGroups)+1):
            RucksackGroup.append(ElfGroups[index-1])
            if (index % 3 == 0) & (index != 0):
                sumOfPriorities += self.calculateSingleGroupPriority(RucksackGroup)
                RucksackGroup = []
        return sumOfPriorities


#
exampleGroups = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

print(
    BadgePriorities().proccessAllGroups(exampleGroups)
)


# %%
with open('input.txt') as f:
    realInput = f.read()
BadgePriorities().proccessAllGroups(realInput)

# %%
len(realInput.strip().split('\n'))/3


# %%
