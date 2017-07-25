from math import pi

def circumference(diameter):
    return pi*(float(diameter))

def area(diameter):
    return pi*(float(diameter)/2.0)**2

diameter=input("Enter the diameter of the circle:")

print('The circumference is:', circumference(diameter))
print('The area is:', area(diameter))