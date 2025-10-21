'''
Write a saturation function that clips a value if it goes outside the range -1 to 1.

$ y = \left\{ \begin{align} -1 && x < -1 \nonumber \\ x && -1 \leq x \leq 1 \nonumber \\ 1 && x > 1 \nonumber \end{align} \right. $

Test it in all three cases and print result.
'''

# your function here
def saturate(x):
    if x>1:
        y = 1
    elif x<-1:
        y = -1
    else:
        y = x
    return y

# test upper limit
x = 2
y = saturate(x)
print('Input',x,'output',y)

# test within limits
x = 0.5
y = saturate(x)
print('Input',x,'output',y)

# test lower limit
x = -2
y = saturate(x)
print('Input',x,'output',y)
