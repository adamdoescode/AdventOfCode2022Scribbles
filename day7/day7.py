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
            'File:',
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

dirs: List[str] = []
#list of files of class file
files: List[file] = []

#loop through each line in dir structure print out
currentDirName: str = None
currentDirDepth: int = 0
for line in exampleInput.split('\n'):
    #check if a directory
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
            #sometimes jump down a directory without it being a dir
            pass

    else:
        print('woah another possibility! See the output below')
        print(line)
        break
        
[x.printAttrs() for x in files]

# %%


# %%
with open('./input.txt', 'r') as f:
    actualInput = f.read()

for line in actualInput.split('\n'):
    print(
        len(line.split('-')[0])
    )



# %%


