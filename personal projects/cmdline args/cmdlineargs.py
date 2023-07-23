# https://docs.python.org/3/library/argparse.html ✅ more than enough
# https://realpython.com/command-line-interfaces-python-argparse/ 
# https://www.digitalocean.com/community/tutorials/how-to-use-argparse-to-write-command-line-programs-in-python 
# https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/

import argparse
parser = argparse.ArgumentParser(prog='CommandLineArgs',
                    description='This is a sample program to learn command line argument parsing with python',
                    epilog='Text at the bottom of help')

parser.add_argument('filename') # positional argument
parser.add_argument('-p','--path') # option that takes a value
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()
print(args.filename)
print(args.path)
print(str(args.verbose))

##  some ways to call this
# python cmdlineargs.py -h 
# python cmdlineargs.py --help 
# python cmdlineargs.py "somefilename.md" -p "c:/dsdsd/dsdsd/xs" 
# python cmdlineargs.py "somefilename.md" -p "c:/dsdsd/dsdsd/xs" -v