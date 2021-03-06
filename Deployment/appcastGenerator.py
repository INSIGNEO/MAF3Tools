#Appcast Creator
import os
import sys
import getopt
import glob
from jinja2 import Environment, PackageLoader

def run(params):
    # load jinja environment variable
    env = Environment(loader=PackageLoader('appcast','templates'))
    decorator_template_appcast = env.get_template('appcast.xml')
    dictionaryReplace = {'title':params['application-name'], 
                         'link':params['link'], 
                         'description':params['description'],
                         'version':params['version'], 
                         }
    target_dir = params['output-path']
    output_file_name = os.path.join( target_dir, params['application-name'] + ".xml"  )
    decorator_template_appcast.stream(dictionaryReplace).dump(output_file_name)
    print "Created appcast: " + output_file_name
    pass

def usage():
    print "python appcastGenerator.py -a TestApp -l http://www.myUrl.org/Apps/MyApp.zip -d \"This is a description of the version\" -o c:\myoutputpath\ "
    print "-a, --application-name          set the application name"
    print "-l, --link                      set link in which to put"
    print "-d, --description               set the description between quotes"
    print "-o, --output-path               set output path"
    print "-v, --version                   set the version"
    print "-h, --help          			   show help (this)"
    
def main():
    argvParams = {}
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:l:d:o:v:", ["help", "application-name","link","description","output-path","version"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-a", "--application-name"):
            argvParams['application-name'] = a
        elif o in ("-l", "--link"):
            argvParams['link'] = a
        elif o in ("-d", "--description"):
            argvParams['description'] = a
        elif o in ("-o", "--output-path"):
            argvParams['output-path'] = a
        elif o in ("-v", "--version"):
            argvParams['version'] = a
        else:
            assert False, "unhandled option"
    
    run(argvParams) 

    
if __name__ == '__main__':
    main()

