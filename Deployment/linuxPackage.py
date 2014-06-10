import os
import sys
import getopt
import glob
import shutil
import zipfile
import os.path
import ConfigParser
import subprocess
import re


pathList = []
depList = []

def run(params):
    executablePath = params['executable-path']
    
    #rad values form .ini files
    config = ConfigParser.ConfigParser()
    config.readfp(open(params['config-file']))
    executableFile = os.path.join(executablePath, config.get('parameters', 'executableFile'))
    print "Product to Deploy: " + executableFile
    archive = os.path.join(executablePath, config.get('parameters', 'archive'))
    print "Creating Archive: " + archive
    listOfModules = []
    for module in config.items('listOfModules'):
        listOfModules.append(os.path.join(executablePath, module[1]))
        print "Module To Add: " + module[1]
    listOfPlugins = []
    for plugin in config.items('listOfPlugins'):
        listOfPlugins.append(os.path.join(executablePath, plugin[1]))
        print "Plugin To Add: " + plugin[1]
      
    
    if(params.has_key('path-qt')):
        externalPath = params['path-qt']  
        pathList.append(externalPath[1])
        print "Path to search: " + externalPath[1]
    else:   
        for path in config.items('listOfPath'):
            pathList.append(path[1])
            print "Path to search: " + path[1]
    
    pathList.append(executablePath)
    
     # open the zip file for writing, and write stuff to it
    file = zipfile.ZipFile(archive, "w")
    
    for moduleName in listOfModules:
        findDep(moduleName)
        print "Adding module: " + moduleName + " to the package"
        file.write(moduleName, os.path.basename(moduleName), zipfile.ZIP_DEFLATED)
    for pluginName in listOfPlugins:
        findDep(pluginName)
        baseName = os.path.basename(pluginName)
        name, fileExtension = os.path.splitext(baseName)
        print "Adding plugin: " + pluginName + " to the package"
        file.write(pluginName, "/plugins/" + name + "/" + name + ".mafPlugin", zipfile.ZIP_DEFLATED)
        
    findDep(executableFile)
    depList.append(executableFile);
    depList.append(os.path.join(executablePath,"Menu.mnu"))
    
    #add ui files
    for inFile in glob.glob( os.path.join(executablePath, '*.ui') ):
        baseName = os.path.basename(inFile)
        file.write(inFile, baseName, zipfile.ZIP_DEFLATED)
        print "Adding to package : " + inFile

    #add xml files
    for inFile in glob.glob( os.path.join(executablePath, '*.xml') ):
        baseName = os.path.basename(inFile)
        file.write(inFile, baseName, zipfile.ZIP_DEFLATED)
        print "Adding to package : " + inFile
        
    depList.sort()
    for fileName in depList:
        baseName = os.path.basename(fileName)
        if "KERNEL" in fileName:
            continue
        print "Adding to package: " + fileName
        file.write(fileName, baseName, zipfile.ZIP_DEFLATED)
    print archive + " correctly created!"
    print "GENERATION SUCCESSFUL"
    
    
   
def findDep(fileToCheck):
    print 'finddep'
    lddOut = subprocess.Popen(["ldd", fileToCheck], stdout=subprocess.PIPE).communicate()[0]
    libraries = {}
    for line in lddOut.splitlines():
        match = re.match(r'\t(.*) => (.*) \(0x', line)
        if match:
            libraries[match.group(1)] = match.group(2)
            print libraries[match.group(1)]
            if libraries[match.group(1)] != '':
                depList.append(libraries[match.group(1)])


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
            print o
            print a
        elif o in ("-c", "--config-file"):
            argvParams['config-file'] = a
            print o
            print a
        elif o in ("-q", "--path-qt"):
            argvParams['path-qt'] = a
        else:
            assert False, "unhandled option"

    #sanity check
    
    run(argvParams) 

    
if __name__ == '__main__':
    main()
