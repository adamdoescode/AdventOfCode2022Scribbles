#%%
from typing import List, Dict
import numpy as np

class RopeBridge():
    def __init__(self) -> None:
        '''
        This dict takes advantage of np.array addition to update the head position
        '''
        self.positionInstructionDict = {
            'U': np.array((0,1)),
            'D': np.array((0,-1)),
            'L': np.array((-1,0)),
            'R': np.array((1,0)),
            'Diag': np.array((1,1)) #special case for Tail
        }
        '''
        A RopeBridge object will hold the head and tail positons + history
        '''
        #initialise head positon
        self.HeadPosition = np.array((0,0))
        #history for head position
        self.HeadPositionHistory: List[np.array] = [self.HeadPosition.copy()]
        #initialise tail positon
        self.TailPosition = np.array((0,0))
        #history for tail position
        self.TailPositionHistory: List[np.array] = [self.TailPosition.copy()]
        
    def isTailTouchingHead(self) -> bool:
        '''
        this function checks if the tail is adjacent to the head
        wow thanks copilot, that is a neat solution!!
        Solution is to substract the head position from the tail position
        Then take the absolute of that value, if it's adjacent it will equal 1
        np.all() ensures we care if either the x or y distance == 1 (this covers diagonal)
        We also care if they overlap to it

        I checked this and it seems to work fine.
        '''
        #check if tail is adjacent or on same coord as head
        if np.all(np.abs(self.TailPosition - self.HeadPosition) <= 1):
            #check special case of diagonal
            return True
        else:
            return False

    def updateTailPosition(self) -> np.array:
        '''
        this function updates the tail position based on the HeadPosition
        A little more complicated as the tail can move diagonally
        Just implemented as a series of if statements... not elegant 🙃 Not implemented at all actually! 🤣
        First check if the tail is touching or adjacent to the head
        If it is, we don't have to do anything about Tail's position
        '''
        if self.isTailTouchingHead():
            #return current position
            return self.TailPosition.copy()
        else:
            '''
            Check if the head is above, below, left or right of the tail
            And then move TailPosition in that direction
            '''
            if self.HeadPosition[0] > self.TailPosition[0]:
                #head is to the right of tail
                self.TailPosition[0] += 1
            elif self.HeadPosition[0] < self.TailPosition[0]:
                #head is to the left of tail
                self.TailPosition[0] -= 1
            if self.HeadPosition[1] > self.TailPosition[1]:
                #head is above tail
                self.TailPosition[1] += 1
            elif self.HeadPosition[1] < self.TailPosition[1]:
                #head is below tail
                self.TailPosition[1] -= 1
            return self.TailPosition.copy()
            

    def updateHeadPosition(self, Direction: str, Movement: int) -> np.array:
        '''
        this function updates the head position
        Movement should always be 1
        '''
        try:
            assert Movement == 1
        except AssertionError:
            print('Movement should always be 1')
        #update head position
        self.HeadPosition += self.positionInstructionDict[Direction]
        return self.HeadPosition.copy()

    def printPositions(self, Direction: str = None, Movement: int = None):
        '''some print statements for lazy checking'''
        print(f'Direction: {Direction}\tMovement: {Movement}')
        print(f'HeadPosition: {self.HeadPosition}')
        print(f'TailPosition: {self.TailPosition}')
        print(f'Is tail touching? {self.isTailTouchingHead()}')
        print()

    def updateRopeBridge(self, input: List[str], printPositions: bool = False):
        '''
        this function updates the bridge
        '''
        #iterate through instructions
        instructions = [instruction.split(' ') for instruction in input]
        for Direction, Movement in instructions:
            #set movement to int
            Movement = int(Movement)
            #update head position
            '''When Movement > 1 we need to update the head position Movement times'''
            if Movement > 1:
                for i in range(Movement):
                    self.HeadPosition = self.updateHeadPosition(Direction, 1)
                    self.TailPosition = self.updateTailPosition()
                    #update history
                    self.HeadPositionHistory.append(self.HeadPosition.copy())
                    self.TailPositionHistory.append(self.TailPosition.copy())
            else:
                self.HeadPosition = self.updateHeadPosition(Direction, Movement)
                self.TailPosition = self.updateTailPosition()
                #update tail position
                self.TailPosition = self.updateTailPosition()
                #update history
                self.HeadPositionHistory.append(self.HeadPosition.copy())
                self.TailPositionHistory.append(self.TailPosition.copy())
            if printPositions:
                self.printPositions(Direction, Movement)


#read in exampleInput.txt
with open('exampleInput.txt', 'r') as f:
    exampleInput = f.read().splitlines()

ropes = RopeBridge()
ropes.updateRopeBridge(exampleInput)
len(set([tuple(x) for x in ropes.TailPositionHistory]))
# %%
with open('input.txt', 'r') as f:
    actualInput = f.read().splitlines()

ropesActual = RopeBridge()
ropesActual.updateRopeBridge(exampleInput)
len(set([tuple(x) for x in ropesActual.TailPositionHistory]))

# %%
'''
Let's test the behaviour of Tailposition?
'''

