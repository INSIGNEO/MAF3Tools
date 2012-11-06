#####################################################
# mafGitHookUtility.py
# author: Alberto Losi
#####################################################

import subprocess

def __git(commands):
    # execute a git command
    p = subprocess.Popen(['git'] + commands, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

def __status(params):
    # execute git status command with specified parameters
    out = __git(['status'] + params)
    return out
    
def getAddedFileNames():
    # get the added files
    statusFiles = __status(['-s'])
    statusFiles = set(statusFiles.splitlines())
    result = []
    for f in statusFiles:
        if(f != '' and f != "''" and f[0] == 'A'): # Not empty added file
            result.append(f[3:len(f)])
    return result

def getModifiedFileNames():
    # get the added files
    statusFiles = __status(['-s'])
    statusFiles = set(statusFiles.splitlines())
    result = []
    for f in statusFiles:
        if(f != '' and f != "''"): # Not empty added file
            result.append(f[3:len(f)])
    return result

def __fileIsA(fileName,ext):
    if(fileName[len(fileName)-len(ext):len(fileName)].lower() == ext.lower()):
        return True
    return False

def fileIsACxx(fileName):
    return __fileIsA(fileName,'cpp') or __fileIsA(fileName,'cxx') or __fileIsA(fileName,'c')
