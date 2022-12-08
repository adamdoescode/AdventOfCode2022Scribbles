#%%
from typing import List, Dict
from anytree import Node, RenderTree
from anytree.importer import DictImporter
importer = DictImporter()
#read in example input
with open('./exampleInput.txt', 'r') as f:
    exampleInput = f.read()

exampleInput
# %%

class file():
    '''
    Class to hold properites (attributes) of files we find in the structure
    Don't think this will need any methods
    '''
    def __init__(self, name:str, size:str, dir:str)  -> None:
        self.name: str = name
        #size comes in as a str so we convert to int here
        self.size: int = int(size)
        self.dir: str = dir
    
    def printAttrs(self):
        '''Just a way to print the attributes if needed'''
        print(
            f'Name:\t{self.name}',
            f'size:\t{self.size}',
            f'dir:\t{self.dir}',
            sep='\t'
        )

class NoSpaceOnDevice():
    '''
    Solver class for day7 problem
    '''
    def __init__(self) -> None:
        self.possibleCommands: dict = {
            'cd': 'move into dir',
        }

    def findCommandsInInput(self, input: str) -> List[tuple[str]]:
        '''
        Parses the puzzle input into something more machine readable
        '''
        commandIdentifier="$"
        commandAndOutput = []
        #split by $ and then 
        for combinedString in input.split(commandIdentifier)[1:]:
            #split so that command is seperate to the other outputs
            if '\n' in combinedString:
                command, allOutputs = combinedString.split('\n', maxsplit=1)
                allOutputs = allOutputs.split('\n')
            else:
                command, allOutputs = (combinedString, None)
            commandAndOutput.append((command, allOutputs))
        return commandAndOutput

    def buildDirNode(self, dirName: str, dirList: List) -> Node:
        '''
        Build up a directory tree from inputs
        Requires dirTree as input?
        '''
        if dirName != '/':
            #get parentDir from Nodes list
            parentNode: Node = dirList[-1]
            newNode = Node(dirName, parent=parentNode)
        else:
            #initialise root node dir
            newNode = Node(dirName)
        return newNode

    def processCommands(self, input) -> None:
        '''
        Takes raw input and then:
        1. passes it to findCommandsInInput
        2. goes through each Cmd + Output pair
        3. 

        3. adds any directories to the directory tree (dirTree, held in dirList)
        4. creates file objects for any files
        5. puts files into the fileList
        '''
        dirList: List[Node] = [] #holds dir objects
        fileList: List[file] = [] #holds file objects
        processedInput = self.findCommandsInInput(input)
        for combinedCmdAndOutput in processedInput:
            command, outputList = combinedCmdAndOutput
            if 'cd' in command:
                if '..' not in command:
                    #isolate dir
                    dirName = command.split(' ')[-1]
                    #create a new Node
                    dirList.append(self.buildDirNode(dirName, dirList))
                else:
                    #go up 1 level




        


#NoSpaceOnDevice().findCommandsInInput(exampleInput)
NoSpaceOnDevice().processCommands(exampleInput)


# %%

myNode = Node('/')
for dirN in ['a','b','c']:
    myNode = Node()


# %%

c = Node('c')
c.children = [Node('l'), Node('k')]
c.children.append(Node('y'))
# %%
data = {
    'a': 'root',
    'children': [{'a': 'sub0',
                  'children': [{'a': 'sub0A', 'b': 'foo'}, {'a': 'sub0B'}]},
                 {'a': 'sub1'}]}

root = importer.import_(data)
print(RenderTree(root))
# %%









# %%

class file():
    '''
    Class to hold properites (attributes) of files we find in the structure
    Don't think this will need any methods
    '''
    def __init__(self, name:str, size:str, dir:str)  -> None:
        self.name: str = name
        #size comes in as a str so we convert to int here
        self.size: int = int(size)
        self.dir: str = dir
    
    def printAttrs(self):
        '''Just a way to print the attributes if needed'''
        print(
            f'Name:\t{self.name}',
            f'size:\t{self.size}',
            f'dir:\t{self.dir}',
            sep='\t'
        )

def createNewFile(line, DirName):
    '''Makes a new file given input of line'''
    return file(
                name=line.split('-')[-1].split('(')[0].strip(),
                size=line.split('size=')[-1].split(')')[0],
                dir=DirName
            )

def getFiles(input: str):
    '''
    Extract file names, sizes, and which directory they are in
    '''

    dirs: List[str] = []
    #list of files of class file
    files: List[file] = []

    #loop through each line in dir structure print out
    currentDirName: str = None
    currentDirDepth: int = 0
    #DirFileSize holds the result we care about
    #we have to initialise the keys in DirFileSize first:
    #iterate through the file structure line by line
    for line in input.split('\n'):
        #check if line is a directory
        if '(dir)' in line:
            #get dir name
            dirName = line.split('-')[-1].split(' (d')[0].strip()
            dirs.append(dirName)
            #set current Dir Name to new name
            currentDirName = dirName
            currentDirDepth = len(line.split('-')[0])
        #check if a file
        elif 'file' in line:
            #need to detect indentation to use to detect what dir we are in
            currentLineDepth = len(line.split('-')[0])
            if currentLineDepth == currentDirDepth:
                #then the currentDirName remains the same
                #create a new file which we add to the files list
                newFile=createNewFile(line, currentDirName)
                files.append(newFile)
            elif currentLineDepth < currentDirDepth:
                #when it is not equal we need to go backwards until we get the right dirname
                #we can find the higher level dir by dividing number of indents by 2
                dirsIndex = int(len(line.split('-')[0])/2)-1
                currentDirName = dirs[dirsIndex]
                newFile=createNewFile(line, currentDirName)
                files.append(newFile)
            elif currentLineDepth > currentDirDepth:
                #this means the file is the first in the current Dir
                newFile=createNewFile(line, currentDirName)
                files.append(newFile)
                currentDirDepth = currentLineDepth

        else:
            print('woah another possibility! See the output below')
            print(line)
            break
            
    [x.printAttrs() for x in files]

getFiles(exampleInput)

# %%
'''
Try to use `anytree` to implement tree structure I can use to determine structure for file sizes
'''

from anytree import Node, RenderTree

root = Node("root")
a = Node("a", parent=root)
e = Node("e", parent=a)
d = Node("d", parent=root)
print(RenderTree(root))

aNodeListExample = [root,a,e,d]
[aNodeListExample]

# %%
from anytree import Node, RenderTree

def findParentDirFromIndentation(currentLineIndentation: int, previousLineIndentation: int, dirs: List[str]) -> str:
    '''
    Function to find the parent directory using:
    - current line's indentation
    - the previous line's indentation
    '''
    parentDir: str = None
    if currentLineIndentation > previousLineIndentation:
        #then previous dir is the parent
        parentDir = dirs[-1]
    elif currentLineIndentation < previousLineIndentation:
        #then we need to find the parent using the currentLineIndentation as an index
        parentDir = dirs[int(currentLineIndentation/2)-1]
    return parentDir
        
    #if 

def getDirTree(input):
    '''
    Extract the Directory tree structure using anytree to store this information
    '''
    #a list to hold our directories
    #root directory is always the bottom directory
    dirTree: Dict[str:Node] = {}
    #this holds a list of dir names
    #Use None to represent top level
    dirNames: List[str] = []
    currentDirName: str = None
    parentDirName: str = None
    currentDirDepth: int = 0
    previousDirDepth: int = 0
    translateRoot = {'/':'root'} #annoying name for root dir

    for line in input.split('\n'):
        if '(dir)' in line:
            #get dir name
            currentDirName = line.split('-')[-1].split(' (d')[0].strip()
            #need to retrieve parent dir
            currentDirDepth = len(line.split('-')[0])
            parentDirName: str = findParentDirFromIndentation(currentDirDepth, previousDirDepth, dirNames)
            #set current Dir Name to new name
            if currentDirName != '/':
                #get parentDir from Nodes list
                parentNode: Node = dirTree[parentDirName]
                newNode = Node(currentDirName, parent=parentNode)
            else:
                #initialise root node dir
                newNode = Node(currentDirName)
            dirTree[currentDirName] = newNode
            #update some variables for the next loop
            previousDirDepth = currentDirDepth
            dirNames.append(currentDirName)
    return dirTree

dirTreeDict: Dict[str,Node] = getDirTree(exampleInput)

for pre, fill, node in RenderTree(dirTreeDict['/']):
    print("%s%s" % (pre, node.name))

# %%
with open('./input.txt', 'r') as f:
    actualInput = f.read()

for line in actualInput.split('\n'):
    print(
        len(line.split('-')[0])
    )



# %%

'''
Turns out I actually need to make the directory output first...
'''

