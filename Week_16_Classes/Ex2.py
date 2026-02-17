'''
The code below can be used to represent a vector. Re-write it to make use of classes. 
You'll need to also edit the tests to work with your class based approach.

import math

def vector_length(vector):
    return math.sqrt(sum(x ** 2 for x in vector))

def vector_addition(vector1, vector2):
    return [x + y for x, y in zip(vector1, vector2)]

def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def test_vectors():

	vector1 = [3, 4]
	vector2 = [1, 2]
	assert(vector_length(vector1)==5)
	assert(vector_length(vector2))==math.sqrt(5)
	assert(vector_addition(vector1, vector2)==[4, 6])
	assert(dot_product(vector1, vector2)==11)

test_vectors()

Re-write the code above to use classes.
'''

class Vector:
    #Your code goes here.


def test_vectors():
    #Your code goes here - tests should be identical to the code above, but re-written to work with vector objects.