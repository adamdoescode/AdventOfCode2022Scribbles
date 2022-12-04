
#%%
from typing import List
#%%
'''
Alternate approach could use a scipy function for determing sets of things, 
we would need to expand out each set to do this I think.
'''


class ContainedAssignmentPairs():
    def findPairs(self, assignedPairs: str) -> List:
        indicatedPairs = [] #list to hold pairs that meet our conditions
        #find all the pairs where one is a superset of the other
        #each row is a pair
        for pair in assignedPairs.strip().split('\n'):
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

    def sumPairs(self, assignedPairs: str) -> int:
        indicatedPairs = self.findPairs(assignedPairs)
        return len(indicatedPairs)


exampleInput = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

ContainedAssignmentPairs().sumPairs(exampleInput)

# %%
with open('input.txt') as f:
    input = f.read()
