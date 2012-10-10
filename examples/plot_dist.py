"""
Just a nice filled plot

Taken from
https://github.com/raoulb/sympy_ipython_notebooks/blob/master/Distributions.ipynb
"""

from sympy.stats import *
import numpy as np
import matplotlib.pyplot as plot

def plot_dist(rv, urange):
    f = density(rv)
    # Fails for piecewise objects!
    #F = lambdify([D[0]], f, "numpy")

    u = np.linspace(urange[0], urange[1], 500)
    #v = F(u)
    v = map(lambda x: float(f(x).evalf()), u)

    m = np.amax(v)

    col = list(np.random.rand(3))

    plot.figure()
    plot.fill_between(u,np.zeros(u.shape),v, color=col+[0.5])
    plot.plot(u,v, color=col)
    plot.grid(True)
    plot.xlim(urange)
    plot.ylim([0.0, 1.1*m])
    plot.yticks(visible=False)

def plot_velocity_distribution():
    from kinematics_uncertain import v
    plot_dist(v, (27, 33))
    plot.title('Distribution of velocity')
