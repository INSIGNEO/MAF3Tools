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

def run(params):
    executablePath = params['executable-path']
    
    
    #rad values form .ini files
    config = ConfigParser.ConfigParser()
    config.readfp(open(params['config-file']))
    productName = os.path.join(executablePath, config.get('parameters', 'productName'))
    print "Product to Deploy: " + productName
    archive = os.path.join(executablePath, config.get('parameters', 'archive'))
    print "Creating Archive: " + archive
    folderName = os.path.splitext(config.get('parameters', 'archive'))[0]
    print "Folder Name: " + folderName
	
    listOfExecutables = []
    for executable in config.items('listOfExecutables'):
        listOfExecutables.append(os.path.join(executablePath, executable[1]))
        print "Executable To Add: " + executable[1]
    listOfModules = []
    for module in config.items('listOfModules'):
        listOfModules.append(os.path.join(executablePath, module[1]))
        print "Module To Add: " + module[1]
    listOfPlugins = []
    for plugin in config.items('listOfPlugins'):
        listOfPlugins.append(os.path.join(executablePath, plugin[1]))
        print "Plugin To Add: " + plugin[1]
    listOfExtraFile = []	
    for extrafile in config.items('listOfExtraFiles'):
        listOfExtraFile.append(extrafile[1])
        print "Extrafile: " + extrafile[1]
    listOfExtraFileLocalPath = []	
    for extrafilelocalpath in config.items('listOfExtraFilesLocalPath'):
        listOfExtraFileLocalPath.append(extrafilelocalpath[1])
        print "Extrafile Local Path: " + extrafilelocalpath[1]  
    
    if(params.has_key('path-qt')):
        externalPath = params['path-qt']  
        pathList.append(externalPath[1])
        print "Path to search: " + externalPath[1]
    else:   
        for path in config.items('listOfPath'):
            pathList.append(path[1])
            print "Path to search: " + path[1]
        
    pathList.append(os.path.join(os.environ["SYSTEMROOT"], "System32"))
    pathList.append(executablePath)
    
     # open the zip file for writing, and write stuff to it
    file = zipfile.ZipFile(archive, "w")
	
    for executableName in listOfExecutables:
        findDep(executableName)
        #depList.append(executableName);
        print "Adding executable: " + executableName + " to the package"
        file.write(executableName, os.path.join(folderName,os.path.basename(executableName)), zipfile.ZIP_DEFLATED)
	
    for moduleName in listOfModules:
        findDep(moduleName)
        print "Adding module: " + moduleName + " to the package"
        file.write(moduleName, os.path.join(folderName,os.path.basename(moduleName)), zipfile.ZIP_DEFLATED)
    for pluginName in listOfPlugins:
        findDep(pluginName)
        baseName = os.path.basename(pluginName)
        name, fileExtension = os.path.splitext(baseName)
        print "Adding plugin: " + pluginName + " to the package"
        file.write(pluginName, os.path.join(folderName,"/plugins/" + name + "/" + name + ".mafPlugin"), zipfile.ZIP_DEFLATED)
      
    #findDep(executableFile)
    #depList.append(executableFile);
    #depList.append(os.path.join(executablePath,"Menu.mnu"))
    
    #add ui files
    #for inFile in glob.glob( os.path.join(executablePath, '*.ui') ):
    #    baseName = os.path.basename(inFile)
    #    file.write(inFile, os.path.join(folderName,baseName), zipfile.ZIP_DEFLATED)
    #    print "Adding to package : " + inFile

    #add xml files
    #for inFile in glob.glob( os.path.join(executablePath, '*.xml') ):
    #    baseName = os.path.basename(inFile)
    #    file.write(inFile, os.path.join(folderName,baseName), zipfile.ZIP_DEFLATED)
    #    print "Adding to package : " + inFile

    counter = 0
    for extraFileName in listOfExtraFile:
        print "Adding to package: " + os.path.join(os.path.join(folderName,listOfExtraFileLocalPath[counter]), os.path.basename(extraFileName))
        file.write(extraFileName, os.path.join(os.path.join(folderName,listOfExtraFileLocalPath[counter]), os.path.basename(extraFileName)), zipfile.ZIP_DEFLATED)
        counter = counter + 1
	    
		
    depList.sort()
    for fileName in depList:
        baseName = os.path.basename(fileName)
        if "KERNEL" in fileName:
            continue
        print "Adding to package: " + fileName
        file.write(fileName, os.path.join(folderName,baseName), zipfile.ZIP_DEFLATED)
    print archive + " correctly created!"
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
    print "-e, --executable-path          set the path with the executable to be packaged"
    print "-c, --config-file              set the absolute path of the configuration file (.ini) for the product"
    print "-h, --help          			  show help (this)"
    print "-q, --path-qt          		  set qt path from command line"
    
def main():
    argvParams = {}
    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:c:q:", ["help", "executable-path","config-file","path-qt"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--executable-path"):
            argvParams['executable-path'] = a
        elif o in ("-c", "--config-file"):
            argvParams['config-file'] = a
        elif o in ("-q", "--path-qt"):
            argvParams['path-qt'] = a
        else:
            assert False, "unhandled option"

    #sanity check
    
    run(argvParams) 

    
if __name__ == '__main__':
    main()
