import os
import sys
import getopt
import glob
import shutil
import zipfile
import pefile
import os.path

#ParabuildCustomCO = "D:/Devel/VPHOP"
pathList = []
depList = []


def run(exeFileName, zipFileName):   

    ParabuildCustomCO = os.environ["PARABUILD_CHECKOUT_DIR"]
    # open the zip file for writing, and write stuff to it
    file = zipfile.ZipFile(zipFileName, "w")
    pathList.append(ParabuildCustomCO)
    pathList.append("C:/Qt/4.7.2/bin/")
    pathList.append("D:/Qt/4.7.2/bin/")
    pathList.append("C:/Qt/4.7.3/bin/")
    pathList.append("D:/Qt/4.7.3/bin/")
    pathList.append(os.environ["SYSTEMROOT"] + "/System32/")
    pathList.append(ParabuildCustomCO + "/../MAF/MAF.Build/build/bin/Release/")
    findDep(exeFileName)
    depList.append(exeFileName);
    depList.append(ParabuildCustomCO + "/../MAF/MAF.build/build/bin/Release/Menu.mnu");
    depList.sort()
    for fileName in depList:
        print "Adding to zip file: " + fileName
        file.write(fileName, os.path.basename(fileName), zipfile.ZIP_DEFLATED)
  
    print "GENERATION SUCCESSFUL"
    
    
   
def findDep(fileToCheck):

    print "Find dependencies of  " + fileToCheck
    pe = pefile.PE(fileToCheck)
    numberOfDep = len(pe.DIRECTORY_ENTRY_IMPORT)
    while (numberOfDep > 0):       
        for fileName in pe.DIRECTORY_ENTRY_IMPORT:
            numberOfDep = numberOfDep - 1
            fileName = fileName.dll
            for item in pathList:
                if os.path.exists(os.path.join(item, fileName)):
                    file_found = 1
                    if not os.path.join(item, fileName) in depList:
                        depList.append(os.path.join(item, fileName))
                    if not os.environ["SYSTEMROOT"] in item and not "/Qt/" in item:
                        print fileName + " found in " + item + "\n"
                        findDep(os.path.join(item, fileName));
                    break
             
             
   
    

def usage():
    print "python hyperMonitorwindowsPackage.py exeFileName zipFileName"
    print "-h, --help                 show help (this)"

    

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
    run(args[0], args[1]) 

    
    
    
if __name__ == '__main__':
    main()
