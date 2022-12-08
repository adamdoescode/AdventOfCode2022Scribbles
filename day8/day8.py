#%%
from typing import List

# %%

class findVisibleTrees():
    def buildYAxis(self, input: List[str]):
        '''
        Takes the input and builds y axis rows
        This allow us to iterate across the y axis easily
        Although actual opperation on y axis will be max()
        Note will need to split by the tree we are inspecting
        '''
        yAxis: List[str] = []
        #iterate across x axis
        for i in range(len(input)):
            #iterate across y axis, adding char to yAxis[i]
            for j in range(len(input[i])):
                try:
                    yAxis[j] += input[i][j]
                except IndexError:
                    yAxis.append(input[i][j])
        return yAxis

    def checkTreeVisible(self, treeHeight, x, y, input, yAxis):
        '''
        We need to check each tree in four dimensions
        So first we split the axis and yAxis by the tree we are inspecting
        Then we test height in each direction
        '''
        #get xAxis row
        xAxisRow = input[x]
        #get yAxis row
        yAxisRow = yAxis[y]
        #split x axis by tree x position
        xAxisSplit: List[str] = [xAxisRow[:x], xAxisRow[x+1:]]
        #split y axis by tree y position
        yAxisSplit: List[str] = [yAxisRow[:x], yAxisRow[x+1:]]
        #check height in each direction
        for trees in xAxisSplit+yAxisSplit:
            intTrees = [int(tree) for tree in trees]
            if int(treeHeight) > max(intTrees):
                print(f"Tree of height {treeHeight} at {x},{y} is visible")
                return True

    def findVisible(self, rawInput):
        input = rawInput.splitlines()
        treeCounter = 0
        #build y axis
        yAxis = self.buildYAxis(input)
        #iterate across x axis
        for x in range(1,len(input)-1):
            #iterate across y axis
            for y in range(1,len(input[x])-1):
                treeHeight = input[x][y]
                #check if tree is visible 
                if self.checkTreeVisible(treeHeight, x, y, input, yAxis):
                    treeCounter += 1
        #calculate outer dimensions to get outer visible trees
        xlen = len(input[0])
        ylen = len(input)
        visibleOuterTrees = (xlen*2) + (ylen-2)*2
        return treeCounter + visibleOuterTrees


#read in exampleInput
with open("exampleInput.txt", "r") as f:
    exampleInput = f.read()

findVisibleTrees().findVisible(exampleInput)

# %%
'''
This tree shouldn't be visible... Tree of height 3 at 1,6 is visible
xAxisLeft = [324262]
yAxisUp = [4]
Okay so the problem is with the buildYAxis function
Not quite sure what it's doing wrong yet...
'''

with open("input.txt", "r") as f:
    input = f.read()
findVisibleTrees().findVisible(input)
# %%

'''Debug yaxis function'''

testExampleInput = exampleInput.splitlines()

findVisibleTrees().buildYAxis(testExampleInput)

# %%
