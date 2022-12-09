#%%
from typing import List

# %%

'''
I missing a tree from the example input:
"The right-middle 3 is visible from the right."
[x,y] = [2,3]
'''

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
        Part 2 class
        We need to check each tree in four dimensions
        So first we split the axis and yAxis by the tree we are inspecting
        Then we test height in each direction
        '''
        #get xAxis row
        xAxisRow = input[x]
        #get yAxis row
        yAxisRow = yAxis[y]
        #split x axis by tree x position
        xAxisSplit: List[str] = [xAxisRow[:y], xAxisRow[y+1:]]
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
    
    def getScenicScore(self, treeHeight, x, y, input, yAxis):
        '''
        Part 2 class
        We are trying to get scenic scores for each interior tree
        '''
        #get xAxis row
        xAxisRow = input[x]
        #get yAxis row
        yAxisRow = yAxis[y]
        '''
        Because we need to consider the trees going *out* from the tree of interest,
        we need to have some directions reversed but not others.
        Need to reverse: Up and Left, but not down and right.
        '''
        #split x axis by tree x position
        treesAxis = {
            'left': xAxisRow[:y][::-1],
            'right': xAxisRow[y+1:],
            'up': yAxisRow[:x][::-1],
            'down': yAxisRow[x+1:]
        }
        scencicDistance = {
            'left': 0,
            'right': 0,
            'up': 0,
            'down': 0
        }

        for key in treesAxis:
            trees = treesAxis[key]
            if trees == '':
                scencicDistance[key] = 1
            else:
                for treeIndex, tree in enumerate(trees):
                    '''We want to find the first tree that is as tall or taller than our tree'''
                    if int(treeHeight) <= int(tree):
                        #then record distance
                        scencicDistance[key] = treeIndex
                        break










        # for direction, trees in treesAxis.items():
        #     if trees == '':
        #         scencicDistance[direction] = 1
        #     else:
        #         #convert tree char to int
        #         intTrees = [int(tree) for tree in trees]
        #         print(intTrees)
        #         for treeIndex, tree in enumerate(intTrees):
        #             if int(treeHeight) <= int(tree):
        #                 #then record distance
        #                 scencicDistance[direction] = len(trees[:treeIndex])
        #                 break
        print(f"Tree of height {treeHeight} at {x},{y}")
        print(treesAxis)
        print(scencicDistance)
        return sum(scencicDistance.values())
        
        # # xAxisSplit: List[str] = [left (reversed), right]
        # xAxisSplit: List[str] = [xAxisRow[:y][::-1], xAxisRow[y+1:]]
        # #split y axis by tree y position
        # # yAxisSplit: List[str] = [up (reversed), down]
        # yAxisSplit: List[str] = [yAxisRow[:x][::-1], yAxisRow[x+1:]]
        # #iterate across each direction until we find a tree the same height or taller
        # print(TreesAxis)
        # distanceVisible: List[int] = []
        # for trees in xAxisSplit+yAxisSplit:
        #     if trees == '':
        #         distanceVisible.append(1)
        #     else:
        #         intTrees = [int(tree) for tree in trees]
        #         for treeIndex, tree in enumerate(intTrees):
        #             if int(treeHeight) <= int(tree):
        #                 #then record distance
        #                 distanceVisible.append(len(trees[:treeIndex])+1)
        #                 break
        # print(f"Tree of height {treeHeight} at {x},{y} is visible {distanceVisible} in each direction")
        # return sum(distanceVisible)

    
    def findMostScenic(self, rawInput):
        input = rawInput.splitlines()
        scenicTrees = []
        #build y axis
        yAxis = self.buildYAxis(input)
        #iterate across x axis
        for x in range(len(input[0])):
            #iterate across y axis
            for y in range(len(input[x])):
                treeHeight = input[x][y]
                #get the tree's scenic score
                scenicScore = self.getScenicScore(treeHeight, x, y, input, yAxis)
                


#read in exampleInput
with open("exampleInput.txt", "r") as f:
    exampleInput = f.read()

# findVisibleTrees().findVisible(exampleInput)
findVisibleTrees().findMostScenic(exampleInput)

# %%
with open("input.txt", "r") as f:
    input = f.read()
findVisibleTrees().findVisible(input)
# %%

'''Debug yaxis function - this now works'''

testExampleInput = exampleInput.splitlines()

findVisibleTrees().buildYAxis(testExampleInput)

# %%
