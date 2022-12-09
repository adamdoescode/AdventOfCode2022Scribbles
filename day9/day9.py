#%%
from typing import List
import numpy as np

# %%

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
    
    def isTailTouchingHead(self, TailPosition: np.array, HeadPosition: np.array) -> bool:
        '''
        this function checks if the tail is adjacent to the head
        wow thanks copilot, that is a neat solution!!
        Solution is to substract the head position from the tail position
        Then take the absolute of that value, if it's adjacent it will equal 1
        np.any() ensures we care if either the x or y distance == 1 (this covers diagonal)
        We also care if they overlap to it
        '''
        #check if tail is adjacent or on same coord as head
        if np.any(np.abs(TailPosition - HeadPosition) <= 1):
            return True
        else:
            return False

    def updateTailPosition(self, TailPosition: np.array, HeadPosition: np.array) -> np.array:
        '''
        this function updates the tail position based on the HeadPosition
        A little more complicated as the tail can move diagonally
        '''
        #check if tail is touching head
        if not self.isTailTouchingHead(TailPosition, HeadPosition):
            #then we must move Tail as appropiate
            pass
            return TailPosition.copy()
        else:
            #do nothing to tail position
            return TailPosition.copy()

    def updateHeadPosition(self, Direction: str, Movement: int, HeadPosition: np.array) -> np.array:
        '''
        this function updates the head position
        Movement should always be 1
        '''
        try:
            assert Movement == 1
        except AssertionError:
            print('Movement should always be 1')
        #update head position
        HeadPosition += self.positionInstructionDict[Direction]
        return HeadPosition.copy()


    def updateRopeBridge(self, input: List[str]):
        '''
        this function updates the bridge
        '''
        #initialise head positon
        HeadPosition = np.array((0,0))
        #history for head position
        HeadPositionHistory: List[np.array] = []
        HeadPositionHistory.append(HeadPosition.copy())
        #initialise tail positon
        TailPosition = np.array((0,0))
        #history for tail position
        TailPositionHistory: List[np.array] = []
        TailPositionHistory.append(TailPosition.copy())
        #iterate through instructions
        instructions = [instruction.split(' ') for instruction in input]
        for Direction, Movement in instructions:
            #set movement to int
            Movement = int(Movement)
            #update head position
            '''When Movement > 1 we need to update the head position Movement times'''
            if Movement > 1:
                for i in range(Movement):
                    HeadPosition = self.updateHeadPosition(Direction, 1, HeadPosition)
                    TailPosition = self.updateTailPosition(TailPosition, HeadPosition)
                    #update history
                    HeadPositionHistory.append(HeadPosition.copy())
            else:
                HeadPosition = self.updateHeadPosition(Direction, Movement, HeadPosition)
                TailPosition = self.updateTailPosition(TailPosition, HeadPosition)
                #update tail position
                TailPosition = self.updateTailPosition(TailPosition, HeadPosition)
                #update history
                HeadPositionHistory.append(HeadPosition.copy())
            #some print statements for lazy checking
            print(f'Direction: {Direction}\tMovement: {Movement}')
            print(f'HeadPosition: {HeadPosition}')
            print(f'TailPosition: {TailPosition}')
            print()


#read in exampleInput.txt
with open('exampleInput.txt', 'r') as f:
    exampleInput = f.read().splitlines()
exampleInput

RopeBridge().updateRopeBridge(exampleInput)

# %%
with open('input.txt', 'r') as f:
    actualInput = f.read().splitlines()
actualInput

# %%
