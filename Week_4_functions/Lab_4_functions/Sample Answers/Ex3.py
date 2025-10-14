'''
Find the solution of the equation below numerically.

$ 10e^{\frac{x}{10}} + x - 17 = 0$

Suggested approach:
 - Implement the expression above as a function
 - You'll need `from math import exp` before you can use the exponential function
 - Write a function to find the lowest integer $x$ such that the solution is in the interval $x$ and $x+1$
 - Write a function that reduces the interval further using a bisection search, i.e. halving it at every step
 '''

from math import exp

def func(x):
    return 10*exp(0.1*x) + x - 17

def find_bracket():
    low_limit = 0
    while func(low_limit+1)<0:
        low_limit = low_limit + 1
    return low_limit

def bisect_bracket(low_limit,high_limit):
    while high_limit>low_limit+0.00001:
        midpoint = 0.5*(high_limit+low_limit)
        if func(midpoint)<0:
            low_limit = midpoint
        else:
            high_limit = midpoint
    return low_limit, high_limit

low_limit = find_bracket()
print('Root is between',low_limit,'and',low_limit+1)
print(func(low_limit),func(low_limit+1))

low_limit, high_limit = bisect_bracket(low_limit,low_limit+1)
print('Root is between',low_limit,'and',high_limit)
print(func(low_limit),func(high_limit))
