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

def energy(x):
    rad = np.linalg.norm(x[0:2])
    spd = np.linalg.norm(x[2:4])
    return 0.5*spd*spd - G*M/rad    

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
    v0 = sqrt(G*M/r0)
    print(f'V0={v0}')
    # initial state
    x0 = np.array([r0,0,0,v0])
    # initial energy
    e0 = energy(x0)
    # error stores
    delta_e_euler = {}
    delta_e_rk4 = {}
    # timestep
    for time_step in [0.1,0.3,1,3,10,30,100,300,600,900]:
        # sim length
        num_steps = int(5400/time_step)
        # Euler
        x_store_euler = solve_steps(step_euler,x0,num_steps,time_step)
        delta_e_euler[time_step] = abs(energy(x_store_euler[:,-1]) - e0)
        print(f'Energy error from Euler with timestep {time_step}: {delta_e_euler[time_step]}')
        # RK4
        x_store_rk4 = solve_steps(step_rk4,x0,num_steps,time_step)
        delta_e_rk4[time_step] = abs(energy(x_store_rk4[:,-1]) - e0)
        print(f'Energy error from RK with timestep {time_step}: {delta_e_rk4[time_step]}')
    # scipy
    output = solve_ivp(f_gravity_wrap_t,[0,num_steps*time_step],x0,method=scipy_method)
    delta_e_scipy = energy(output.y[:,-1]) - e0
    print(f'Energy error from scipy({scipy_method}): {delta_e_scipy}')
    # trajectory plots
    fig,ax = plt.subplots(1,2)
    ax[0].plot(x_store_euler[0,:],x_store_euler[1,:])
    ax[0].plot(x_store_rk4[0,:],x_store_rk4[1,:],'g')
    ax[0].plot(output.y[0,:],output.y[1,:],'r')
    ax[0].plot(0,0,'go')
    ax[0].axis('equal')
    ax[0].legend(('Euler','Runge-Kutta',f'scipy ({scipy_method})'))
    # error comparison
    ax[1].loglog(delta_e_euler.keys(),delta_e_euler.values(),'-o')
    ax[1].loglog(delta_e_rk4.keys(),delta_e_rk4.values(),'-go')
    ax[1].legend(('Euler','Runge-Kutta'))
    plt.show()

if __name__=='__main__':
    if len(sys.argv)!=2:
        main()
    else:
        main(sys.argv[1])
