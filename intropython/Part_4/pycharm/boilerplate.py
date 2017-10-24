##BOILER PLATE

## '__main__' is the name of the scope in
## which top-level code executes.
## A module’s __name__ is set equal
## to '__main__' when read from standard
## input, a script, or from an interactive
## prompt.

## When Python interpreter reads a source file,
## it will execute all the code found in it.

## When Python runs the "source file" as the
## main program, it sets the special variable
## (__name__) to have a value ("__main__").
## When you execute the main function,
## it will then read the "if" statement and
## checks whether __name__ does equal to __main__.

## In Python "if __name__== "__main__" allows you
## to run the Python files either as reusable
## modules or standalone programs.

## If you import the python code:
## 1) __name__= module's filename
## 2) if statement==false
## 3) The script in __main__ will not be executed

## If you directly run the python code:
## 1) __name__=__main__
## 2) if statement == True,
## 3) the script in 'hello()' will be executed
## So when the code is executed, it will check
## for module name with "if."

##THIS IS THE CALLER (boiler_caller.py)

import boilerplate

#boilerplate.main()
boilerplate.hello()

## THIS IS THE MODULE (boilerplate.py)

def hello() :
    print("Hello World")

def main():
    print("Main function executes")

print ("Hello Mars")

print("__name__ is set to: ", __name__)

#if __name__ == "__main__" :
#    hello()

if __name__ == "__main__" :
    main()