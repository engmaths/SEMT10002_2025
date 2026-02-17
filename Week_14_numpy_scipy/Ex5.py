'''
Lotka-Volterra model

The Lotka-Volterra equations can be used to describe the population of a predator-prey system. 
If we use x to represent the population density of the prey animal, and y to represent the population density of the predator, 
then the equations describing the model are:

dx/dt = (alpha * x) - (beta *  x * y)
dy/dt = (delta * x * y) - (gamma * y)

where alpha describes the birth rate of the prety, beta the effect of the predator on the preys growth rate, delta the predator's death rate, 
and gamma the effect of the prey on the predators growth rate. 

Write a program to solve the Lotka-Volterra system. 
When run from the terminal, your code should use sensible default values to solve the equation, producing a plot to show the output.
'''