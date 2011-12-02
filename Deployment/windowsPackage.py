import os
import sys
import getopt
import glob
import shutil
import zipfile
import pefile
import os.path
import ConfigParser

pathList = []
depList = []

def run(configFileName):   

    ParabuildCustomCO = os.environ["PARABUILD_CHECKOUT_DIR"]
    #ParabuildCustomCO = "D:/parabuildCustomCO/MAF3_VPHOP_CODES_VS9REL/"
    
    #rad values form .ini files
    config = ConfigParser.ConfigParser()
    config.readfp(open(configFileName))
    inputExeFile = ParabuildCustomCO + config.get('parameters', 'inputExeFile')
    print "EXE TO DEPLOY: " + inputExeFile
    outputZipFile = ParabuildCustomCO + config.get('parameters', 'outputZipFile')
    print "ZIP TO CREATE: " + outputZipFile
    listOfPlugin = []
    for plugin in config.items('listOfPlugin'):
        listOfPlugin.append(ParabuildCustomCO + "/MAF.Build/build/bin/Release/" + plugin[1])
        print "PLUGIN TO ADD: " + plugin[1]
    for path in config.items('listOfPath'):
        pathList.append(path[1])
        print "PATH TO SEARCH: " + path[1]
    pathList.append(os.environ["SYSTEMROOT"] + "/System32/")
    pathList.append(ParabuildCustomCO + "/MAF.Build/build/bin/Release/")
    
     # open the zip file for writing, and write stuff to it
    file = zipfile.ZipFile(outputZipFile, "w")
    
    for pluginName in listOfPlugin:
        findDep(pluginName)
        baseName = os.path.basename(pluginName)
        name, fileExtension = os.path.splitext(baseName)
        print "ADDING TO PACKAGE PLUGIN: " + pluginName
        file.write(pluginName, "/plugins/" + name + "/" + name + ".mafPlugin", zipfile.ZIP_DEFLATED)
       
    findDep(inputExeFile)
    depList.append(inputExeFile);
    depList.append(ParabuildCustomCO + "/MAF.build/build/bin/Release/Menu.mnu");
    depList.sort()
    for fileName in depList:
        baseName = os.path.basename(fileName)
        if "KERNEL"in fileName:
            continue
        print "ADDING TO PACKAGE: " + fileName
        file.write(fileName, baseName, zipfile.ZIP_DEFLATED)
    print outputZipFile + " correctly created!"
    print "GENERATION SUCCESSFUL"
    
    
   
def findDep(fileToCheck):
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
                        
                        if not "System32" in item:
                            depList.append(os.path.join(item, fileName))
                            print fileName + " found."
                            findDep(os.path.join(item, fileName));
                    break
             

def usage():
    print "python hyperMonitorwindowsPackage.py configFile.ini"
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
    run(args[0]) 

    
if __name__ == '__main__':
    main()
