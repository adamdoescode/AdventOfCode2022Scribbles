
#%%
from typing import List, Dict

# %%

class cargoCraneShifter():

    def stackPrettyPrint(self, stack: Dict) -> None:
        for key in stack:
            print(f'{key}: {stack[key]}')
    
    def processStacks(self, rawStacks: str) -> Dict[int,List]:
        '''
        Takes raw string of just the stacks and turns them into a Dict[List] data structure to process
        '''
        rowLen = len(rawStacks.split('\n')[0])
        stacks = {stackIndex:[] for stackIndex in range(1,int((rowLen+1)/4)+1)}
        for stackIndex, stackChars in enumerate(range(2,rowLen,4)):
            for row in rawStacks.split('\n'):
                item = row[stackChars-2:stackChars+1].replace('[','').replace(']','')
                if item != '   ':
                    stacks[stackIndex+1].append(item)
        #remove extra indexes and reverse stack order
        for stackKey in stacks:
            stacks[stackKey] = list(reversed(stacks[stackKey][:-1]))
        return stacks

    def processInput(self, input: str) -> Dict:
        '''
        Takes the string input and returns a dict where each part is composed of appropiate objects
        '''
        intermediateInput = input.split('\n\n')
        parts = ['stacks','instructions']
        InputSplitDict = {part: inputItem for part,inputItem in zip(parts,intermediateInput)}
        ##then fix up each of the parts
        ##fix the stack
        InputSplitDict['stacks'] = self.processStacks(InputSplitDict['stacks'])
        ##the instructions
        InputSplitDict['instructions'] = InputSplitDict['instructions'].split('\n')
        return InputSplitDict

    def shiftCargo(self, processedInput) -> List:
        '''
        Takes the processed input and returns the shifted stack
        '''
        stacks = processedInput['stacks']
        instructions = processedInput['instructions']
        self.stackPrettyPrint(stacks)
        for instruction in instructions:
            #extract instruction steps
            numbers = [int(number) for number in instruction.split(' ') if number.isdigit()]
            step = dict(zip(['move','from','to'],numbers))
            print(step)
            #perform the instruction
            #pop step['move'] entries from stack['from'] and append to stack['to']
            itemToMove = list(reversed(stacks[step['from']][-step['move']:]))
            #update the stack we just took from
            stacks[step['from']] = stacks[step['from']][:-step['move']]
            #update the stack we just moved to
            stacks[step['to']] = stacks[step['to']] + itemToMove
            self.stackPrettyPrint(stacks)
            
    def shiftCargo9001(self, processedInput) -> List:
        '''
        Same process, but we now consider do not reverse the item to move
        '''
        stacks = processedInput['stacks']
        instructions = processedInput['instructions']
        self.stackPrettyPrint(stacks)
        for instruction in instructions:
            #extract instruction steps
            numbers = [int(number) for number in instruction.split(' ') if number.isdigit()]
            step = dict(zip(['move','from','to'],numbers))
            print(step)
            #perform the instruction
            #pop step['move'] entries from stack['from'] and append to stack['to']
            itemToMove = list(stacks[step['from']][-step['move']:])
            #update the stack we just took from
            stacks[step['from']] = stacks[step['from']][:-step['move']]
            #update the stack we just moved to
            stacks[step['to']] = stacks[step['to']] + itemToMove
            self.stackPrettyPrint(stacks)

        return stacks

    def coordinateCraneCalculation(self, input: str, CrateMover9001 = False) -> List:
        processedInput = self.processInput(input)
        if CrateMover9001:
            shiftedCargo = self.shiftCargo9001(processedInput)
        else:
            shiftedCargo = self.shiftCargo(processedInput)
        topCrates = []
        for stackKey in shiftedCargo:
            topCrates.append(shiftedCargo[stackKey][-1])
        #topCrates = [stack[-1] for stack in shiftedCargo]
        return topCrates


exampleInput = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

#cargoCraneShifter().coordinateCraneCalculation(exampleInput)
cargoCraneShifter().coordinateCraneCalculation(exampleInput, CrateMover9001 = True)

#%%
stackEg = exampleInput.split('\n\n')[0]
cargoCraneShifter().processStacks(stackEg)

# %%
'''
wow this is an annoying format lol i need to think about it...

The top of most stacks is empty, this is represented by \s\s\s.
The seperator is \s
So for the top row in example input we have:
\s\s\s\s[D]\s\s\s\s
Where:
\s\s\s[\s][D][\s]\s\s\s

Well I could just take each stack as a set of 3 chars? Yes!
With a 1 char gap between them... so:
'''
stackEg = exampleInput.split('\n\n')[0]
rowLen = len(stackEg.split('\n')[0])
stacks = {stackIndex:[] for stackIndex in range(int((rowLen+1)/4))}
for stackIndex, stackChars in enumerate(range(2,rowLen,4)):
    for row in stackEg.split('\n'):
        stacks[stackIndex].append(row[stackChars-2:stackChars+1])

stacks

# %%
cargoCraneShifter().processStacks(stackEg)
# %%
with open('input.txt') as f:
    input = f.read()

''.join(cargoCraneShifter().coordinateCraneCalculation(input.strip(), CrateMover9001 = True))
# %%
