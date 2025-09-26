'''
## Exercise 3 - Collision Detection

If we have a circle centered at point $(u,v)$ and with radius $R$, we can calculate whether another point $(x, y)$ 
is inside the circle by checking whether the Euclidean distance between the points 
(i.e Pythagoras theorem for the hypotenuse - distance = $\sqrt((x-u)^2 + (y-v)^2)$) is less than the radius. 
Unfortunately, taking a square root is *not* one of the fundamental operations we have available to us, 
(we'll see how to use the square root function soon).

Without using the square root function, complete the code below to test whether the point (x,y) is with radius R of point (u,v).
'''

x = 0
y = 0
u = 1
v = 0
R = 1

#There's more than one way to do this, but the easiest is to realise that we can square both sides of the inequality.
print((x-u)**2 + (y-v)**2 <= R**2) 
