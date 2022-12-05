
#%%
from typing import List
#%%
'''
Alternate approach could use a scipy function for determing sets of things, 
we would need to expand out each set to do this I think.
'''


class ContainedAssignmentPairs():
    def printPairs(self, pairs):
        print(
            pairs
        )
    
    def findPairs(self, assignedPairs: str) -> List:
        indicatedPairs = [] #list to hold pairs that meet our conditions
        #find all the pairs where one is a superset of the other
        #each row is a pair
        for pair in assignedPairs:
            assignment1, assignment2 = pair.split(',')
            #each start and stop is seperated by a "-"
            #we want them to be integers so we use a tuple comprehension to assign them as int
            assignment1Start, assignment1End = (int(number) for number in assignment1.split('-'))
            assignment2Start, assignment2End = (int(number) for number in assignment2.split('-'))
            #test if assignment1 is a subset of assignment2
            if (assignment1Start >= assignment2Start) & (assignment1End <= assignment2End):
                #then assignment1 is a subset
                indicatedPairs.append((assignment1, assignment2))
            elif (assignment1Start <= assignment2Start) & (assignment1End >= assignment2End):
                #then assignment2 is a subset
                indicatedPairs.append((assignment1, assignment2))
            else:
                pass
        return indicatedPairs

    def sumPairs(self, indicatedPairs: List) -> int:
        '''this works for both parts'''
        return len(indicatedPairs)
    
    def processRawInput(self, rawInput: str) -> List:
        return [pair for pair in rawInput.strip().split('\n')]

    def itemGenerator(self, start,stop) -> str:
        return [x for x in range(start,stop+1)]

    def findAnyPairs(self, assignedPairs: str) -> List:
        indicatedPairs = []
        for pair in assignedPairs:
            assignment1, assignment2 = pair.split(',')
            #each start and stop is seperated by a "-"
            #we want them to be integers so we use a tuple comprehension to assign them as int
            assignment1Start, assignment1End = (int(number) for number in assignment1.split('-'))
            assignment2Start, assignment2End = (int(number) for number in assignment2.split('-'))
            
            #brute force it
            assignment1Items = self.itemGenerator(assignment1Start, assignment1End)
            assignment2Items = self.itemGenerator(assignment2Start, assignment2End)
            for item in assignment1Items:
                if item in assignment2Items:
                    indicatedPairs.append((assignment1, assignment2))
                    break
        return indicatedPairs

    def calculateAnyOverlap(self, input: str, part1 = True) -> List:
        PairList = self.processRawInput(input)
        if part1:
            indicatedPairs = self.findPairs(PairList)
            return self.sumPairs(indicatedPairs)
        else:
            #part 2
            indicatedPairs = self.findAnyPairs(PairList)
            return self.sumPairs(indicatedPairs)


exampleInput = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

ContainedAssignmentPairs().calculateAnyOverlap(exampleInput, part1 = False)

# %%
with open('input.txt') as f:
    input = f.read()

ContainedAssignmentPairs().calculateAnyOverlap(input, part1 = False)

# %%
ContainedAssignmentPairs().itemGenerator(6,8)

# %%
