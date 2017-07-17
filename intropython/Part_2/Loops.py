# LOOPS

## A loop is a construct to execute some code for
## every item of a sequence. Let's start to discuss
## loops by introducing `for` loop

for i in [1,"blue",2.9,True,"winter is coming"]:
    print(i)


## Let's say we have a list variable with some
## string items in it. We want to capitilize
## all items. We can still do it without a loop.

animals = ['chicken', 'sheep', 'goat', 'llama']
print(animals[0].upper())
print(animals[1].upper())
print(animals[2].upper())
print(animals[3].upper())


## As you can see, this is pretty ugly because
## we are repeating ourselves and this will be no
## fun to type if our list had, say, 100 items in it.


## Let's try with a `for` loop:

for animal in animals:
    print(animal.upper())


## The `for .. in` statement takes each element of a
## sequence or other "iterable" variable, assigns the
## element temporarily to the name you specify ("animal" in
## this instance), and executes the statements in the indented block.


## When that block is finished executing for a given value
## of the sequence, the next value in the sequence gets
## assigned to the variable you created and the statements
## in the block are run again, and on and on until the
## sequence runs out of values.


## We can loop over lots of different kinds of things in Python.

## Dictionaries (by key):

animal_names = {'dog': 'Rex', 'rat': 'Willard', 'turtle': 'Leonardo'}
for species in animal_names:
    print("The", species, "is named", animal_names[species])


## Strings (by character):

alpha = "abcdefg"
for letter in alpha:
    print(letter)

## Strings (by words):

lyrics = "I did it my way"
for word in lyrics.split(" "):
    print(word.upper())


## `break` is a special statement which is used to
## terminate the loops from inside before all items
## are processed over

for i in (1,2,3,4,5,6,7,8):
    print(i)
    if i==4:
        break
    print('loop continues')


## `continue` is another special statement that is
## used inside the for loop. This statement indicates that
## the loop will skip to the next item on the list
## without executing the rest of the actions for the current item.

for i in (1,2,3,4,5,6,7,8):
    print(i)
    if i==4:
        continue
    print('loop continues')


## We have seen `else` statement in connection
## with `if` conditional. `else` can also be used
## with `for` loop. The action given with
## the `else` statement is executed when
## the loop terminates without any `break`

for i in (1,3,5,7):
    print(i)
    if i==4:
        break
else:
    print('loop completed')


for i in (1,2,3,4,5,6):
    print(i)
    if i==4:
        break
else:
    print('loop completed')


## The python syntax allows for looping over more than
## one variable at the same time.

for (i,j) in [('a',1.6),('k',2),('q',122)]:
    print(i)
    print(j)


## Another widely used loop construct is `while`.
## This loop executes as long as the condition its
## given is true or until a `break` is encountered

## Below a `while` loop is executed until "count"
## variable becomes 10. Once this value hits 10,
## the condition "count < 10" becomes false and
## the `while` statement stops executing.
## The mechanism to increase "count" is to add one
## to its value at each iteration.

count = 0
while count < 10:
    print("!", end="") # The "end" keyword argument here prevents the
                       # print function from emitting a newline character
    count += 1 


## We can use `continue` and `break` excatly same as `for` loop.
## `continue` will move the iteration to the next check on the
## logical condition given by the `while` and `break` will
## cause the loop to terminate immediately.

i = 0
while i < 10:
    i += 1
    if (i==4) or (i==8): continue
    print(i)


i = 0
while i < 10:
    i += 1
    if (i==4): break
    print(i)
print("loop completed")


## The use of `else` is also same in `while` and `for` loops.

j = 8
i = 0
while i < j:
    i += 1
    if (i==10): break
    print(i)
else:
    print("j is less than 10")

