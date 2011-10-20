import os
import sys
import getopt

skipConditions = { "alreadyExecutable":"@executable_path/",
	           "systemLibrary":"/System/Library/Frameworks/",
	           "usrLibPath":"/usr/lib/",
	         }

param = {}

def needToBeFixed(l):
    for i in skipConditions.values():
        if(i in l):
            return False;
    
    return True

def fixObjectFile(fileName):
    # check each line of the result of otool -L and see if it is a binary object
    #if yes OK
    #if no... check inside the bundle and use the path @executable/../<somePath> in install_name_tool
    #install_name_tool -change "oldname" "newname" target.dylib or .so 
    
    # otool -L over each file
    otoolOutputFileName = "otoolFileResult_" + fileName.split("/")[-1].split(".")[0]
    #print otoolOutputFileName
    otoolCommand = "otool -L " + fileName + " > " + otoolOutputFileName
    os.system(otoolCommand)
    
    
    #check each result
    f = open(otoolOutputFileName)
    lines = f.readlines()
    for line in lines:
        if(needToBeFixed(line)):
            searchStr = " (compatibility" # there is a space at the beginning
            searchStringIndex = line.find(searchStr)
            if(searchStringIndex != -1):
                fullpathObjectName = line[:searchStringIndex]
                objectName = fullpathObjectName.split("/")[-1]
                command = "install_name_tool -change " + fullpathObjectName + " @executable_path/../Frameworks/" + objectName + " " + fileName
                #print command
                #import time
                #time.sleep(5)
                os.system(command)
    f.close()
    #remove otool file result
    os.remove(otoolOutputFileName)



def run():    
    bundleDir = param['bundle']
    #search for all files ("is not an object file")
    for path, subdirs, files in os.walk(bundleDir):
        for name in files:
            fullPath = os.path.join(path, name)
            fixObjectFile(fullPath)

def usage():
    print "python macInstallLibBundle.py -b bundle"
    print "-h, --help                 show help (this)"
    print "-b, --bundle=           select the bundle to be fixed"
    

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:", ["help", "bundle="] )
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-b", "--bundle"):
            param['bundle'] = os.path.abspath(os.path.normpath(a))
        else:
            assert False, "unhandled option"
    
    if(len(param) == 0):
        usage()
        #print currentPathScript
        return
    
    run()
    
    
if __name__ == '__main__':
    main()
