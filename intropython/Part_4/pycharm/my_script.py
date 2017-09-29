## SCRIPTING
## Here we are going to look at how we
## can divide our script and create modules
## if needed.


## VERSION 1 (everything is together in my_script.py)

## This is my_script.py

#from os import getcwd
#import datetime

#a=datetime.datetime.now()

#print("""The execution location: {1}
#Execution time: {0}""".format(a,getcwd()))


## VERSION 2 (Create my_script.py, my_module.py, my_module2.py)

## This is my_script.py

#import my_module
#import my_module2

## This is my_module.py

#import datetime

#a=datetime.datetime.now()
#print('Execution time: {0}'.format(a))

## This is my_module2.py

#from os import getcwd

#print('The execution location: {0}'.format(getcwd()))

## VERSION 3 (Create my_script.py, my_module.py, my_module2.py)

## This is my_script.py

#from my_module import print_time
#from my_module2 import print_path

#print_time()
#print_path()

## This is my_module.py

#import datetime

#def print_time():
#    a=datetime.datetime.now()
#    print('Execution time: {0}'.format(a))

## This is my_module2.py

#from os import getcwd

#def print_path():
#    print('The execution location: {0}'.format(getcwd()))

## VERSION 4 (Create my_script.py, my_module.py, my_module2.py)

## This is my_script.py

from my_module import print_time
from my_module2 import print_path

#help(print_time)
#print(print_time.__doc__)

print_time(print_path())

## This is my_module.py

#import datetime
#
#def print_time(my_path):
#    a=datetime.datetime.now()
#    print('Execution time: {0}'.format(a))
#    print(my_path)
#    return

## This is my_module2.py

#from os import getcwd

#def print_path():
#    return 'The execution location: {0}'.format(getcwd())
