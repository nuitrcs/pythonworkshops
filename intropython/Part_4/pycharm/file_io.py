## THIS FILE IS FOR PYTHON IO TRAINING

## Through out this training we have used `print`
## statement to produce output that is created during
## run time.

## We have seen print statements as below:

my_lucky_number=948
print('My lucky number is', my_lucky_number)

## A different method to do the same is to use
## string.format() method

my_lucky_number=948
print('My lucky number is {0}'.format(my_lucky_number))

## The argument order inside format() can be passed into the
## string in the order that coder defined. Variable names can
## also be used (see variable `otherperson` below) instead
## of

print('My name is {1}, your name is {0}, and his name is \
{otherperson}'.format('Janna', 'Alper', otherperson='Boby'))

print('My name is {1}, your name is {0}, and his name is '
      '{otherperson}'.format('Janna', 'Alper', otherperson='Boby'))

my_pi=3.14159265359
print('Pi is equal to {0:10.4f}'.format(my_pi))

my_pi=3.14159265359
print('Pi is equal to {0:10.7f}'.format(my_pi))

## An old formatting style
my_pi=3.14159265359
print('Pi is equal to %10.7f' % my_pi)


## We could also provide data to Python
## from outside.

## The built-in function `input()` can be used
## to read from the standard input channel.

your_name=input("Enter your name:")
print("Your name is:", your_name)

## Another kind of interaction of the code with
## the outside world is through files.

## The simplest and easiest kind of data to work with is
## accessing files on the same computer as your script.
## Python has a built-in way to open files, the
## open() function.

## open() returns a "file object", which is basically
## a thing that knows how to read and write the file
## whose name you pass into the open() function.

## fp = open(filename,mode)

## The first argument to open() is the path to the file
## to open, and the second argument is the "mode" which
## identifies your intention to open the file. The mode
## is usually one of the following:
##    'r' for read-only
##    'w' to write to a file by overwriting
##    'a' to write to a file by appending at the end
##    'r+' to read and write

## A file object has methods. `write()` takes a
## message and writes to the file object. `close()`
## method closes the pipe to the file.

msg1='First line of file'

fp = open('log.txt','w')
fp.write(msg1)
fp.write('\n')

# fp.write(msg1,'\n') # Show fileobject.write() takes exactly one argument
# fp.write(msg1+'\n') # but this is acceptable

msg2='Second line of file'
fp.write(msg2)
fp.write('\n')

print(fp.closed) # We are querying if the file is closed

if (not fp.closed):
    fp.close() # Don't forget to close your files when you are done

print(fp.closed) # We are querying if the file is closed

## Two lines are written to log.txt file

fp = open('log.txt','w')
msg3='Third line of the file'
fp.write(msg3)
fp.write('\n')

fp.close()

## As you see we overwrote the two lines we had
## in the file. Let's try appending

fp = open('log.txt','a')
msg4='Fourth line of the file'
fp.write(msg4)
fp.write('\n')

fp.close()

## Let's look at some other methods of
## file objects

## `read()` returns the entire contents of the file

## `readline()` returns one line at a time from the file.

## `tell()` returns the current position of the file
## read/write pointer within the file

## `seek()` changes the position in the file object.
## fp.seek(offset, from_what) : from_what indicates
## the reference point, offset is the position to be
## moved reference to from_what. from_what can be 0
## (default, beginning of the file), 1 (current position)
## and 2 (end of file)


fp = open('log.txt','r')

print(fp.read(1))
print(fp.read(1))
print('Current position in the file:', fp.tell())
fp.seek(1, 0)
print('Current position in the file:', fp.tell())
print(fp.readline())

print(fp.read())

fp.closed

if (not fp.closed): # We are querying if the file is closed
    fp.close

## Closing file:
# - Avoids using unnecessary system resources
# in the form of file descriptors on handles
# - Avoids race conditions and code failures
# depending on the access rights

## If you don't want to concern about
## closing the file use `with open() as`
## statement

with open('with_open.txt', 'w') as my_file:
    my_file.write("with open('filename', 'mode') as fileobject \n")
    my_file.write("You don't need to worry about closing the file")

if my_file.closed :
    print('my_file is closed')


## JSON (JavaScript Object Notation)

## The json library can parse JSON from
## strings or files. The library parses
## JSON into a Python dictionary or list.
## It can also convert Python dictionaries
## or lists into JSON strings.

import json

my_string = '{"first_name": "Zaphod", "last_name":"Beeblebrox",\
 "occupation":"Galactic President"}'

print("my_string type is: ", type(my_string))

parsed_json = json.loads(my_string)

print(parsed_json,type(parsed_json))
print('What is the name of Galactic President:', parsed_json['first_name'])

my_dictionary = {
    'first_name': 'Zaphod',
    'second_name': 'Beeblebrox',
    'occupation': ['Galactic President', 'Thief'],
}

## serializing
print(json.dumps(my_dictionary))
print(type(json.dumps(my_dictionary)))

with open('serialized.txt', 'w') as serialized_wfile:
    json.dump(my_dictionary, serialized_wfile)

## deserializing
with open('serialized.txt', 'r') as serialized_rfile:
    other_dictionary = json.load(serialized_rfile)
    print(other_dictionary, type(other_dictionary))