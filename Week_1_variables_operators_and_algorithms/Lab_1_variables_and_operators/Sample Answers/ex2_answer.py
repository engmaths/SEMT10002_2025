'''
Exercise 2 - Floating Point Comparisons

We saw the following code in this week's notes, observing that it produces the incorrect output. 
As a reminder, this is due to the limited precision by which floating point numbers are stored, 
meaning that in general, we should avoid using the ```==``` operator with floats. 

A better way to compare if two floats are equal to is to see whether the difference between in them is small 
("small", will be context dependent, but let's assume less than $10^-5$ for today). 
Re-write the code below to do the comparison correctly.
'''

e = 5/9
f = (1/3)*5*(1/3)
print('e is', e)
print('f is', f)
print(e-f < 10**-5) # This works, but be careful- if f is bigger than e (i.e e-f is negative), it'll always be true
print(((e-f)**2)**0.5 < 10**-5) #A better solution instead looks at the absolute value of the difference.