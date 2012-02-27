import os
import sys
import getopt

skipConditions = { """"alreadyExecutable":"@executable_path/","""
	           "systemLibrary":"/System/Library/Frameworks/",
	           "usrLibPath":"/usr/lib/",
	         }

param = {}

def needToBeFixed(l):
    for i in skipConditions.values():
        if(i in l):
            return False;  
    return True
    
def initBundle(bundleDir):
    # replace macdeployqt mechanism, this application copy all the files necessary to the bundle    
    # MAF dylibs, already present thanks to CMAKE
    # plugins, for the moment copy all the plugins directory
    binDir =  os.path.join(bundleDir, "..")
    executableDir = os.path.join(bundleDir, "Contents", "MacOS")
    pluginsDirSrc = os.path.join(binDir, "plugins")
    pluginsDirDst = os.path.join(executableDir, "plugins")
    import shutil
    try:
        shutil.rmtree(pluginsDirDst)
    except:
        pass
    shutil.copytree(pluginsDirSrc, pluginsDirDst)
    
    #ui files
    uifileList = [file for file in os.listdir(binDir) if file.lower().endswith(".ui")]
    for item in uifileList:
        try:
            os.remove(os.path.join(executableDir,item) )
        except:
            pass
        shutil.copy(os.path.join(binDir,item) , os.path.join(executableDir, item))
    # copy qt share files
    qtDirSrc = param['qt-path']
    qtDirDst = os.path.join(bundleDir, "Contents", "Frameworks")
    try:
        shutil.rmtree(qtDirDst)
    except:
        pass
    shutil.copytree(qtDirSrc, qtDirDst)
    
    #copy qt plugins
    qtPluginsDirSrc = os.path.join(param['qt-path'], "..", "plugins")
    qtPluginsDir = os.path.join(bundleDir, "Contents", "Plugins")
    try:
        shutil.rmtree(qtPluginsDir)
    except:
        pass
    shutil.copytree(qtPluginsDirSrc, qtPluginsDir)
    
    #create Resource/qt.conf
    resourcesDir = os.path.join(bundleDir, "Contents", "Resources")
    if(not os.path.exists(resourcesDir)):
        os.mkdir(resourcesDir)
    f = open(os.path.join(resourcesDir, "qt.conf"), 'w')
    f.write("[Paths]\n")
    f.write("Plugins = PlugIns\n")
    f.close()
    
    #remove _debug and libQtCLucene and QtHelp
    for path, subdirs, files in os.walk(qtPluginsDir):
        for name in files:
            if("_debug" in name):
                fullPath = os.path.join(path, name)
                os.remove(fullPath)
                
    #remove _debug from plugins
    for path, subdirs, files in os.walk(qtDirDst):
        for name in files:
            if("_debug" in name or "libQtCLucene" in name or "QtHelp" in name or name.lower().endswith(".la") or name.lower().endswith(".a")):
                fullPath = os.path.join(path, name)
                os.remove(fullPath)

    #remove useless libraries
    removeList = ["libopencv_highgui", "libopencv_calib3d", "libopencv_contrib", "libopencv_features2d", "libopencv_gpu", "libopencv_legacy", "libopencv_objdetect"]
    for path, subdirs, files in os.walk(executableDir):
        for name in files:
            for l in removeList:
              if(l in name):
                fullPath = os.path.join(path, name)
                try:
                    os.remove(fullPath)
                except:
                    pass
        
    

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
#        print line
        if(needToBeFixed(line)):
            searchStr = " (compatibility" # there is a space at the beginning
            searchStringIndex = line.find(searchStr)
            if(searchStringIndex != -1):
                fullpathObjectName = line[:searchStringIndex]
                
                objectName = fullpathObjectName.split("/")[-1]
                relName = fileName[fileName.index(param['bundle']):]
                if(objectName[:2] == "Qt" or objectName == "phonon" or objectName[:2] == "libQt"):
                        #if("VTKButtons" in fileName.split("/")[-1]):
                        #print   fullpathObjectName
                        #if("QtCore" in fullpathObjectName):

                        qtPathExtension = objectName + ".framework/Versions/4/"
                        command = "install_name_tool -id "  + " @executable_path/../Frameworks/" + qtPathExtension + objectName + " " + param['bundle'] +"/Contents/Frameworks/" + qtPathExtension + objectName
                        os.system(command)
                        command = "install_name_tool -change " + fullpathObjectName + " @executable_path/../Frameworks/" + qtPathExtension + objectName + " " + relName
                        #command = "install_name_tool -change " + " @executable_path/../Frameworks/" + qtPathExtension + objectName + " " + "/Users/dannox/Libraries/QtSDK/Desktop/Qt/474/gcc/lib/" + qtPathExtension + objectName + " "+ relName
                        os.system(command)
                else:
                    command = "install_name_tool -id "  + " @executable_path/" + objectName + " " + os.path.join(param['bundle'], "Contents","MacOS", objectName) 
                    os.system(command)
                    command = "install_name_tool -change " + fullpathObjectName + " @executable_path/" + objectName + " " +  relName
                    os.system(command)
                
    f.close()
    #remove otool file result
    os.remove(otoolOutputFileName)

def run():
    bundleDir = os.path.abspath(os.path.normpath(param['bundle']))
    initBundle(bundleDir)
    
    #search for all files ("is not an object file")
    for path, subdirs, files in os.walk(bundleDir):
        for name in files:
            fullPath = os.path.join(path, name)
            fixObjectFile(fullPath)

def usage():
    print "python macInstallLibBundle.py -b bundle"
    print "-h, --help                 show help (this)"
    print "-b, --bundle=              select the bundle to be fixed"
    print "-q, --qt-path=             select the path from which copy qt shared libs"
    

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:q:", ["help", "bundle=", "qt-path="] )
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
            param['bundle'] = a
        elif o in ("-q", "--qt-path"):
            param['qt-path'] = a
        else:
            assert False, "unhandled option"
    
    if(len(param) == 0):
        usage()
        #print currentPathScript
        return
    
    run()
    
    
if __name__ == '__main__':
    main()
