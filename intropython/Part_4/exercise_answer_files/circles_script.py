from circles_mod import circumference, area

with open('circle_rad.input','r') as finput:
	diameter=2*float(finput.readline())
# circle_rad.input doesn't exist in the repo, you'll have to create it

print('The circumference is:', circumference(diameter))
print('The area is:', area(diameter))

with open('circle_area.output','w') as foutput:
	foutput.write('The circumference is: {}\n'.format(circumference(diameter)))
	foutput.write('The area is: {}\n'.format(area(diameter)))
