from math import pi

def circumference(diameter):
    return pi*(float(diameter))

def area(diameter):
    return pi*(float(diameter)/2.0)**2

with open('circle_dia.input','r') as finput: 
	diameter=float(finput.readline())
# circle_dia.input doesn't exist in the repo, you'll have to create it

print('The circumference is:', circumference(diameter))
print('The area is:', area(diameter))

with open('circle_area.output','w') as foutput:
	foutput.write('The circumference is: {}\n'.format(circumference(diameter)))
	foutput.write('The area is: {}\n'.format(area(diameter)))
