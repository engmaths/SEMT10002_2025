from math import sin, cos

D = 150 # mm
R = 35 # mm

def f(x,y,th,om_l,om_r):
    v = 0.5*R*(om_l + om_r)
    w = (om_l - om_r)*R/D
    x_dot = v*sin(th)
    y_dot = v*cos(th)
    th_dot = w
    return x_dot, y_dot, th_dot

def rk4(x,y,th,om_l,om_r,h):
    k1x,k1y,k1th = f(x,y,th,om_l,om_r)
    k2x,k2y,k2th = f(x+0.5*h*k1x,
                     y+0.5*h*k1y,
                     th + 0.5*h*k1th,
                     om_l,om_r)
    k3x,k3y,k3th = f(x+0.5*h*k2x,
                     y+0.5*h*k2y,
                     th + 0.5*h*k2th,
                     om_l,om_r)
    k4x,k4y,k4th = f(x+h*k3x,
                     y+h*k3y,
                     th + h*k3th,
                     om_l,om_r)
    xo = x + h*(k1x + 2*k2x + 2*k3x + k4x)/6.0
    yo = y + h*(k1y + 2*k2y + 2*k3y + k4y)/6.0
    tho = th + h*(k1th + 2*k2th + 2*k3th + k4th)/6.0
    return xo,yo,tho

x = 0
y = 0
th = 0

om_l = 1
om_r = 0
dt_ms = 13464

for ii in range(dt_ms):
    x,y,th = rk4(x,y,th,om_l,om_r,0.001)

print('x',x,'y',y,'th',th)