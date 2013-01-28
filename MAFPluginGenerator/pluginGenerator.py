
__author__ = 'Daniele Giunchi'

import sys, os
import pprint
from jinja2 import Environment, PackageLoader
from lxml import etree
import re

DEBUG = False

def main( pluginName, target_dir = "./output"):

    pluginName = pluginName.replace('mafPlugin', '').replace('plugin','').replace('Plugin','')
    target_dir = os.path.join(os.path.realpath(target_dir), "mafPlugin" + pluginName)
    
    # load jinja environment variable
    env = Environment(loader=PackageLoader('mafPluginTemplate', 'templates'))
    #cycle all over the templates
    templateDict = {}
    
    for file in os.listdir(os.path.join(os.path.dirname(__file__), 'mafPluginTemplate', 'templates')):
        name = (os.path.basename(file))
        if(name == ".DS_Store"):
            continue
        print "**************" + name + "**************"
        templateDict[name] = env.get_template(name)
    
    classDetails = {'pluginName': pluginName , }

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    print "*** " + target_dir
    # generate plugin stub
    for n in templateDict.keys():
        output_file_name = os.path.join( target_dir, n.replace('PluginTemplate','Plugin' + pluginName).replace('Template','')  )
        templateDict[n].stream(classDetails).dump(output_file_name)


    if DEBUG:
        f = open("debug.txt","w")
        defstdout = sys.stdout
        sys.stdout = f
        for key in templateDict.keys():
            pprint.pprint("something to debug")
        f.close()

        sys.stdout = defstdout


def usage():
    print "\n\n"
    print "\tUsage: %s <name_of_the_plugin> [target_dir]\n" % sys.argv[0]
    print "\t\t%s will look for a template dir and create the stub for a plugin" % sys.argv[0]
    print "arguments: ", sys.argv

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        print "please provide all inputs!"
        sys.exit( -1 )
        
    if len(sys.argv) > 2:
        print "output create in %s" % sys.argv[2]
        main(sys.argv[1], sys.argv[2])
    else:
        print "output create in %s" % os.path.join(os.path.realpath('./output'))
        main(sys.argv[1])
