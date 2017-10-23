## Develop a short python script that calculates the shell area
## between a larger and a smaller circle.

#- The code will read an input file that contains the diameter
# of the large and small circle. The input includes many sets
# of large&small circle radii.

#- The code will have one main script and a module file.
# The main script will do the reading, writing and calling
# the module functions. The module file will contain the
# calculator for the shell area

#- The code will write the output to both screen and an
# output file. No negative value

#- Your input file should look like this:
# 6 4
# 3.3 5.6
# 2 9
# 8.3 9.2
# 3.1 4.4
# 6 5
# 8 11.2
# 7 2

from shell import shell
from area import area

finput = open('shell.input','r')
foutput=open('shell_area.output','w')

for line in finput:
    diameter1=float(line.split()[0])
    diameter2=float(line.split()[1])
    print('The shell area is:', shell(area,diameter1,diameter2))
    foutput.write('The shell area is: ')
    foutput.write(str(shell(area,diameter1,diameter2)))
    foutput.write('\n')

foutput.close()
finput.close()
