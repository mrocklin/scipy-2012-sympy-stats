from sympy import *

x0 = Symbol('x_0')
y0 = Symbol('y_0')
yf = Symbol('y_f')
g = Symbol('g')
v = Symbol('v')
theta = Symbol('theta')

t = Symbol('t')
x = x0 + v * cos(theta) * t
y = y0 + v * sin(theta) * t + g*t**2 / 2
impact_time = solve(y - yf, t)[0]

xf = x0 + v * cos(theta) * impact_time
