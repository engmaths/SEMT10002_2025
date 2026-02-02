import sys
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

G = 6.674e-11 # gravitational constant N(m/kg)^2
M = 5.972e24 # mass of Earth in kg
R = 6371e3 # radius of Earth in m

def f_gravity(x):
    # unpack the state
    pos = x[0:2]
    vel = x[2:4]
    # radius
    r = np.linalg.norm(pos)
    # acceleration
    acc = -G*M*pos/(r**3)
    # state derivative
    return np.concat([vel,acc])

def step_euler(f,x,time_step):
    return x + time_step*f(x)

def step_rk4(f,x,time_step):
    k1 = f(x)
    k2 = f(x+0.5*time_step*k1)
    k3 = f(x+0.5*time_step*k2)
    k4 = f(x+time_step*k3)
    return x + time_step*(k1+2*k2+2*k3+k4)/6

def solve_steps(step_fun,x0,num_steps,time_step):
    # initialise store
    x_store = np.zeros((4,num_steps))
    x = x0
    for ii in range(num_steps):
        x = step_fun(f_gravity,x,time_step)
        x_store[:,ii] = x
    return x_store

def f_gravity_wrap_t(t,x):
    # scipy requires dynamics function of form f(time,state) but ours has no time requirement
    # define a wrapper to re-use our function while discarding the unneeded time argument
    return f_gravity(x)

def main(scipy_method='RK45'):
    # initial alt
    a0 = 300e3
    r0 = R+a0
     # initial speed
    v0 = sqrt(0.9*G*M/r0)
    print(f'V0={v0}')
    # initial state
    x0 = np.array([r0,0,0,v0])
    # timestep
    time_step = 10
    # sim length
    num_steps = 540
    # Euler
    x_store_euler = solve_steps(step_euler,x0,num_steps,time_step)
    # RK4
    x_store_rk4 = solve_steps(step_rk4,x0,num_steps,time_step)
    # scipy
    output = solve_ivp(f_gravity_wrap_t,[0,num_steps*time_step],x0,method=scipy_method)
    # comparison plots
    plt.plot(x_store_euler[0,:],x_store_euler[1,:])
    plt.plot(x_store_rk4[0,:],x_store_rk4[1,:],'g')
    plt.plot(output.y[0,:],output.y[1,:],'r')
    plt.plot(0,0,'go')
    plt.axis('equal')
    plt.legend(('Euler','Runge-Kutta',f'scipy ({scipy_method})'))
    plt.show()

if __name__=='__main__':
    if len(sys.argv)!=2:
        main()
    else:
        main(sys.argv[1])
