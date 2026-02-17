'''
Calculating mean squared error.

In machine learning, it's common to work with models that make predict the value of things- 
for example, we could train a model to predict the number of medals that team GB is expected 
to win at the Olympics, or the number of admissions to hospital on a certain day of the year. 
One way of evaluating such a model is to calculate the mean squared error-this is given by the formula:

MSE = check notes for formula!

Given the following data set, write some *vectorised* code to calculate the mean squared error. 
'''

import numpy as np 
predictions = np.array([4, 5, 6, 1, 2, 6, 8, 9, 10])
actual = np.array([5, 5, 6, 2, 3, 5, 4, 7, 9])

#Your code goes here.