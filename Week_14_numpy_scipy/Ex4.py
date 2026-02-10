'''
A variation on the SIR  model is the SIS model, in which those who recover from the disease can become re-infected again. 
The equations for describing this system are:

dS/dT = (-beta * S * I) / N + (gamma * I)
dI/dT = (beta * S * I) / N - (gamma * I)

Edit the code from the SIR model to solve this system. 
You'll need to define a new function for calculating the gradient (i.e "diff_SIS") and another function to solving the ODE (i.e "solve_SIS"). 
Plot the results of both models on a single figure.
'''

import matplotlib.pyplot as plt 
from scipy.integrate import odeint 
import numpy as np 

#Let's use a population of 1000 people
N = 1000 
#S represents the number of susceptible people; we'll start our model with one infected, with means S=N-1
S = N-1 
#I represents the number of infected people; we'll leave start this at one.
I = 1 
#R represents the number of people removed (either due to recovery or death). We start this at zero.
R = 0 

def diff_sir(sir, t, beta, gamma):

	'''
	Calculates the gradient for an SIR model of disease spread
	Inputs:
		sir: state of the system, with sir[0] = number susceptible
									   sir[1] = number infected
									   sir[2] = number recovered
		t: current time- not used here, but odeint expects to pass this argument so we must include it
		beta: the rate at which the virus spreads
		gamma: the rate at which people are removed due to the virus
	Outputs:
		the gradient of the SIR model
	'''

	dsdt = (-beta*sir[0] * sir[1])/N 
	didt = (beta*sir[0]*sir[1])/N - (gamma * sir[1])
	drdt = gamma * sir[1]

	grad = [dsdt, didt, drdt]

	return grad 

def solve_sir(sir0, t_max, beta, gamma):
	'''
	Solves an SIR model using odeint.
	'''

	t = np.linspace(0, t_max)
	sir = odeint(diff_sir, sir0, t, (beta, gamma))

	return sir, t 

def plot_sir(t, data):

	fig = plt.figure()
	ax1 = fig.add_subplot(311)
	ax1.plot(t, data[:, 0], label='S(t)')
	ax2 = fig.add_subplot(312)
	ax2.plot(t, data[:, 1], label='I(t)')
	ax3 = fig.add_subplot(313)
	ax3.plot(t, data[:, 2], label='R(t)')
	plt.tight_layout()

def main():

	#Set values for model parameters here.
	beta = 0.4
	gamma = 0.2 
	#Let's solve for 100 time steps
	t_max = 100 
	#Create a tuple to represent the initial conditions
	sir0 = (S, I, R)
	#Solve the model
	sir, t = solve_sir(sir0, t_max, beta, gamma)
	#Plot the results
	plot_sir(t, sir)

main()