'''
## Exercise 2 - Circles

Suppose we have three circles in the $xy$-plane:

- Circle $C_1$ is centred at $(0, 0)$ with radius of length 5.
- Circle $C_2$ is centred at $(2, 1)$ and has radius of length 2.
- Circle $C_3$ is centred at $(-5, 0)$ and has a radius of length 3.

The image here (https://raw.githubusercontent.com/engmaths/SEMT10002_2025/refs/heads/main/media/week_2/circles.png) illustrates the arrangement.

> Using conditional statements, write a program which takes in the variables $x$ and $y$ and tells the user which circle(s) the point $(x, y)$ is in.

> Think about the order in which your program evaluates the expressions? Is this the most efficient way to structure the code?
'''

# define a test point
x = 0
y = 0 # in C1, not C2 C3

# define a test point
x = 10
y = 10 # not in any

# define a test point
x = 1
y = 0 # C1 and C2, not C3

# define a test point
x = -1
y = 0 # C1 not C2 or C3

# define a test point
x = -4
y = 0 # C1 and C3 not C2

# define a test point
x = -6
y = 0 # C3 not C1 or C2

# check c2 first as it can tell us everything
if (x-2)**2 + (y-1)**2 <= 2**2:
    print(x,',',y,'in C1 and C2 but not in C3')
else:
    print(x,',',y,'not in C2')
    # check other two separately, could be in either or both
    if x**2 + y**2 <= 5**2:
        print(x,',',y,'in C1')
    else:
        print(x,',',y,'not in C1')
    if (x+5)**2 + y**2 <= 3**2:
        print(x,',',y,'in C3')
    else:
        print(x,',',y,'not in C3')

