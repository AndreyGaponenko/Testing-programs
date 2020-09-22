from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
a=1
def integrand(t, x):
    return np.cos(a*t-x*np.sin(t))
def expint(x):
    return quad(integrand, 0, np.pi, args=(x))
y=np.vectorize(expint(0,5,1)
print(y)