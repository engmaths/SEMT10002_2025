'''
================
Exercise 5
================

Planet  Diameter (km)   Mass (relative to Earth)        Rotation period 
Mercury 4,878           0.06                            58.65 (d) 
Venus   12,100          0.82                            243 (d)  
Earth   12,756          1.00                            23.934 (h)  
Mars    6,794           0.11                            24.623 (h)  
Jupiter 142,800         317.89                          9.842  (h)  
Saturn  120,000         95.17                           10.233 (h)  
Uranus  52,400          14.56                           16 (h) 
Neptune 48,400          17.24                           18 (h)  


1. Write a program that identifies and prints the name of the planet with the lowest density.
  Assume each planet is a perfect sphere
'''

from math import pi

planet = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']


diameter = [4878, 12100, 12756, 6794, 142800, 120000, 52400, 48400]

mass = [0.06, 0.82, 1.00, 0.11, 317.89, 95.17, 14.56, 17.24]

rotation_period = [58.65*24, 243*24, 23.934, 24.623, 9.842, 10.233, 16, 18]

min_density = None

for p, d, m in zip(planet, diameter, mass):

    # Calculate the density
    density = m / (4/3 * pi * (d/2)**3)

    # If a new minimum is identified, store the density and planet name
    if min_density == None or density < min_density:
        min_density = density
        name = p

print('The planet with the lowest density is', name)


'''
2. Write a program that identifies and outputs the names and rotation periods of planets
 with a rotation period shorter than Earth's.
'''

for p, r in zip(planet, rotation_period):
    if p =='Earth':
        earth_rotation = r

for p, r in zip(planet, rotation_period):
    if r < earth_rotation:
        print(p, 'has a shorter rotation period than Earth')


