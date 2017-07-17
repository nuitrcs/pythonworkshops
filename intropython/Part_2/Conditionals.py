# CONDITIONALS & LOOPS

## Now that we have covered data types and sequences,
## let's use loops and conditionals to do some programming.

## Prior to this point we have seen data types and
## collections that are specific to python.

## Conditionals and loops, on the other hand,
## are basic concepts that are used in all well-known coding languages

# CONDITIONALS

## The actions in computer programs adapt changing input
## by the help of conditional statements.

## `if` statement starts a condition in python where
## some action is taken if the condition is satisfied.

if 8>1:
    print('8 is bigger than 1')

if 8<1:
    print('If this is printed, consider using another language')

## As you see the condition (8 < 1) is false and nothing printed

## Parentheses after "if" make the expressions more readable

if (8>1):
    print('8 is bigger than 1')

## There are many other comparison operators,
## equal : `==`,
## not equal : `!=`,
## greater than or equal to : `>=`

if 8>=1:
    print('8 is greater than or equal to 1')


if 8!=1:
    print('8 is not equal to 1')


## Using the words `and`, `or`, `not`, more
## complex conditionals can be written

a=8
b=4
c=5.5
if (b<c<a):
    print('b is smaller than c, c is smaller than a')


a=8
b=4
c=5.5
d=11.99
if(b<c<a) and (d>12):
    print('b is smaller than c but bigger than a and d is bigger than 12')


a=8
if(not a<0):
    print('a is not smaller than 0')


## If an expression evaluates as any of the following,
## it evaluates as False:

## - Empty containers (tuples, sets, dicts and lists), such as [ ], { }
## - Zero-length strings "" (not " ")
## - The values 0 or 0.0
## - The value None
## - The value False

## Most other values evaluates as True

a="" # 0, 0.0, []
if (not a): ## This is equivalent to if (a==0)
    print('Is a zero?')


a=" "
if (a):
    print('a is not zero')


## An `if` statement can be followed by an `else` statement
## or any number of `elif` (i.e. else if) statements

a=0
if (a==0):
    print('zero')
else:
    print('negative or positive')


a=3
if (a==0):
    print('zero')
elif (a>0):
    print('positive')
elif (a<=0):             # This option will never run
    print('negative')


a=3
if (a==0):
    print('zero')
elif (a>0):
    print('positive')
else:            
    print('negative')


## `if`, `elif` and `else` statements must have at least
## one python action

a=3
if (a==0):
#    print('zero')
elif (a>0):
    print('positive')
else:            
    print('negative')


## You could use `pass` clause as a placeholder
## which does nothing

a=0
if (a==0):
    #print('zero')
    pass
elif (a>0):
    print('positive')
else:            
    print('negative')


## In python indentation defines the grouping. Especially if
## you are writing nested arguments, be very careful about the
## indentation level

a=1
b=0
if (a == 0): 
    print("a is zero")
    if (b == 0):
        print("a and b are zero")
else:
    print("a is definitely not zero")


a=1
b=0
if (a == 0): 
    print("a is zero")
    if (b == 0):
        print("a and b are zero")
    else:
        print("a is definitely not zero")


## Python allows single line if statements. For readability
## purposes generally writing an indented code is better practice

a=3
if (a==0): print('zero')
elif (a>0): print('positive')
else: print('negative')