import sys
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

G = 6.674e-11 # gravitational constant N(m/kg)^2
M = 5.972e24 # mass of Earth in kg
R = 6371e3 # radius of Earth in m

# !! your functions here !!

def main(scipy_method='RK45'):
    # initial alt
    a0 = 300e3
    # !! your code here !!

if __name__=='__main__':
    if len(sys.argv)!=2:
        main()
    else:
        main(sys.argv[1])
