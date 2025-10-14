'''
Find the solution of the equation below numerically.

$ 10e^{\frac{x}{10}} + x - 17 = 0$

Suggested approach:
 - Implement the expression above as a function
 - You'll need `from math import exp` before you can use the exponential function
 - Write a function to find the lowest integer $x$ such that the solution is in the interval $x$ and $x+1$
 - Write a function that reduces the interval further using a bisection search, i.e. halving it at every step
 '''