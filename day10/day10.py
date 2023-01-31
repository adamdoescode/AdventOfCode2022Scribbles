
'''
Day 10 code in python

TODO not sure if small example is supposed to be:
[1, 1, 4, 4, -1]
or 
[1, 1, 4, 4, 4, -1]
Assuming former for now.
'''
#%%
class cathodeTube:
    '''Implements the solution'''
    def __init__(self) -> None:
        #instructions we will be interpreting
        self.instructions = {
            "noop": None,
            "addx": 1,
        }
        #instructions modify this register
        self.register = 1
        #records the register value after each instruction
        self.cycles = [self.register]
    
    def parseInstruction(self, instruction:str) -> tuple:
        '''Parses the instruction'''
        #check if the instruction is valid
        if "noop" in instruction:
            return ("noop")
        elif "addx" in instruction:
            number = int(instruction.split(" ")[1])
            return ("addx", number)

    def run(self, instructions:list):
        '''Runs the instructions'''
        for instruction in instructions:
            #parse the instruction
            instructionTuple = self.parseInstruction(instruction)
            #update register
            if instructionTuple[0] == "noop":
                #register stays the same, add it to the cycles list
                self.cycles.append(self.register)
            elif instructionTuple[0] == "addx":
                #this instruction takes 2 cycles
                #in first cycle we do nothing
                #so we add a new cycle with the same value as the previous cycle
                self.cycles.append(self.register)
                # in the second cycle the
                # register is incremented by 1
                self.register += instructionTuple[1]
                self.cycles.append(self.register)
        
    def interestingRegisters(self):
        '''
        The problem asks for information from specific registers:
        20th
        and then every 40th
        Returns an iterable of the values of those registers
        '''
        cycleIndex = 19 #off by one
        while cycleIndex < len(self.cycles):
            yield self.cycles[cycleIndex]
            cycleIndex += 40


# %%
# read in smallExampleInput.txt
with open("smallExampleInput.txt", "r") as f:
    smallExampleInput = f.read().splitlines()
smallExampleInput

smallCathodeTube = cathodeTube()
smallCathodeTube.run(smallExampleInput)
smallCathodeTube.cycles
# %%
# larger example input
with open("largerExampleInput.txt", "r") as f:
    largerExampleInput = f.read().splitlines()

largerCathodeTube = cathodeTube()
largerCathodeTube.run(largerExampleInput)
#largerCathodeTube.cycles
list(largerCathodeTube.interestingRegisters())
# %%
