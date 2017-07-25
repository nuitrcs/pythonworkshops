from shellarea import shellarea

# you can use with to open multiple files at the same time
with open('circle_diameters.txt','r') as finput, \ # the \ lets you put in a line break in the command
	open('shellareas_output.txt', 'w') as foutput:
	for line in finput:
		diameter1, diameter2 = (float(x) for x in line.split())
		print('The shell area is:', shellarea(diameter1, diameter2))
		foutput.write('The shell area is: {}\n'.format(shellarea(diameter1, diameter2)))
		