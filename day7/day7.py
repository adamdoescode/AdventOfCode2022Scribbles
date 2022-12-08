#%%
from typing import List, Dict

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

