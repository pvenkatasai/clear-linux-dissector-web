import os
import sys
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
#print(os.path.normpath(join(os.getcwd(), path)))
print(os.path.abspath(os.path.dirname(sys.argv[0])))
