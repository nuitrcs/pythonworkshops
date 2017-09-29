## You developed a python code including functions
## to calculate circumference and area of a circle.
## Now, divide the code into 2 different parts:

# - First file should be a module that includes
# the functions.

# - Second file should be the main python code that
# takes the input from a file and writes the results
# to both screen and an output file.

import area

finput = open('circle_area.input','r')
diameter2=float(finput.readline())
finput.close

print('The circumference is:', area.circumference(diameter2))
print('The area is:', area.area(diameter2))

foutput=open('circle_area.output','w')

foutput.write('The circumference is: ')
foutput.write(str(area.circumference(diameter2)))
foutput.write('\n')

foutput.write('The area is: ')
foutput.write(str(area.area(diameter2)))

foutput.close