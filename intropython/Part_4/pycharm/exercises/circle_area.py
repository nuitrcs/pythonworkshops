## Write a short script to calculate and print out
## the circumference and area of a circle with only
## diameter as input. You can use `math` module which
## includes constant `pi`. For circumference and area
## calculations develop 2 functions.

# - First develop the code to read the diameter
# interactively (input via keyboard) and print the
# results to screen. Hint: Interactive input is read
# as a string

# - Second, change the code to read the diameter
# from a file and print the results to screen as
# well as to an output file. Hint: file.write()
# method accepts a string

from math import pi

def circumference(diameter):
    return pi*(float(diameter))

def area(diameter):
    return pi*(float(diameter)/2.0)**2

## First part of the exercise

diameter=input("Enter the diameter of the circle:")
print(type(diameter))

print('The circumference is:', circumference(diameter))
print('The area is:', area(diameter))

## Second part of the exercise

finput = open('circle_area.input','r')
diameter2=float(finput.readline())
finput.close

print('The circumference is:', circumference(diameter2))
print('The area is:', area(diameter2))

foutput=open('circle_area.output','w')

foutput.write('The circumference is: ')
foutput.write(str(circumference(diameter2)))
foutput.write('\n')

foutput.write('The area is: ')
foutput.write(str(area(diameter2)))

foutput.close
