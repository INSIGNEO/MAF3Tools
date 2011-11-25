import os
import sys
import getopt
import glob
import shutil
import zipfile


def run():   
    ProgramFile = os.environ["ProgramFiles"]
    System32 = os.environ["SYSTEMROOT"];
    System32 += '/System32'
    #ParabuildCustomCO = os.environ["PARABUILD_CHECKOUT_DIR"]
    ParabuildCustomCO = "D:/Devel/VPHOP"
    
    #remove the deploy directory and create it again
    if os.path.exists(ParabuildCustomCO + "/vphop_codes.build/build/VPHOP/HyperModelMonitor/Deploy"):
        shutil.rmtree(ParabuildCustomCO + "/vphop_codes.build/build/VPHOP/HyperModelMonitor/Deploy")
        
    os.mkdir(ParabuildCustomCO + "/vphop_codes.build/build/VPHOP/HyperModelMonitor/Deploy")
    
    # open the zip file for writing, and write stuff to it
    file = zipfile.ZipFile(ParabuildCustomCO + "/vphop_codes.build/build/VPHOP/HyperModelMonitor/Deploy/HyperMmonitor.zip", "w")
    
    #app .exe
    name = ParabuildCustomCO + "/../MAF/MAF.build/build/bin/Debug/HyperModelMonitor.exe";
    print "adding to zip: " + name
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
    #Menu.mnu
    name = ParabuildCustomCO + "/../MAF/MAF.build/build/bin/Debug/Menu.mnu";
    print "adding to zip: " + name
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
    #Application dll
    for name in glob.glob(ParabuildCustomCO + "/../MAF/MAF.build/build/bin/Debug/*.dll"):
        if 'vtk' not in name:
            print "adding to zip: " + name
            file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        
    #Qt dll
    for name in glob.glob("C:/Qt/4.7.2/bin/*.dll"):
        print "adding to zip: " + name
        file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)    
        
    #python25.dll
    name = System32 + "/python25.dll";
    print "adding to zip: " + name
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
    

def usage():
    print "python hyperMonitorwindowsPackage.py"
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
        
    run()
    
    
if __name__ == '__main__':
    main()
