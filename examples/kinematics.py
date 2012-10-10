from sympy import *

x0 = 0
y0 = 0
yf = -30
g = -10
v = 30
theta = pi/4

t = Symbol('t')
x = x0 + v * cos(theta) * t
y = y0 + v * sin(theta) * t + g*t**2 / 2
impact_time = solve(y - yf, t)[0]

xf = x0 + v * cos(theta) * impact_time
