from sympy import *
from sympy.stats import *
x0 = 0
y0 = 0
yf = -30
g = -10
v = Normal('v', 30, 1)
theta = pi/4

t = Symbol('t', positive=True)
x = x0 + v * cos(theta) * t
y = y0 + v * sin(theta) * t + g*t**2 /2
impact_time = solve(y - yf, t)[1]

xf = x.subs(t, impact_time)
